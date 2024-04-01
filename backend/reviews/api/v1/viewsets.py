from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from restaurant.api.v1.serializers import MenuSerializer
from restaurant.models import Menu
from reviews.api.v1.serializers import ReviewSerializer,UserReviewSerializer
from reviews.models import Review
from utils.decorators import isUser,isOwner
from utils.fetch_id import get_user_id,get_restaurant_id
from django.db.models import Avg
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_406_NOT_ACCEPTABLE,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
class ReviewViewSet(ModelViewSet):
    http_method_names=['get','post']
    queryset=Review.objects.all()
    serializer_class=UserReviewSerializer
    @isUser
    def list(self, request,*args,**kwargs):
        try:
            queryset = self.queryset.filter(user=get_user_id(request)).order_by('-id')
            serializer=self.serializer_class(queryset,many=True)
            try:
                return Response({"message":"All Reiviews","data":serializer.data},status=HTTP_200_OK)
            except:
                return Response({"message":serializer.error_messages},status=HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            return Response({"message":str(e)},status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    @isOwner
    def retrieve(self, request, *args, **kwargs):
        try:
            result = self.queryset.filter(restaurant=get_restaurant_id(request),menu=kwargs.get('pk'))
            serializer=self.serializer_class(result,many=True)
            try:
                return Response({"message":"All Reiviews","data":serializer.data},status=HTTP_200_OK)
            except:
                return Response({"message":serializer.error_messages},status=HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            return Response({"message":str(e)},status=HTTP_500_INTERNAL_SERVER_ERROR)
        
    @isUser
    def create(self, request, *args, **kwargs):
        try:
            result = self.queryset.filter(user=get_user_id(request), menu=request.data['menu'])
            if result:
                return Response({"message":"User Already reviewed"},status=HTTP_200_OK)
            request.data['user']=get_user_id(request)
            rating=request.data['rating']
            queryset=Menu.objects.filter(id=request.data['menu'])
            serializer=MenuSerializer(queryset,many=True)
            request.data['restaurant']=serializer.data[0]['restaurant']
            if rating<0.0:
                request.data['rating']=0.0
            elif rating>5.0:
                request.data['rating']=5.0
            serializer=ReviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"Reiview added successfully","data":serializer.data},status=HTTP_201_CREATED)
            return Response({"message":serializer.error_messages},status=HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            return Response({"message":str(e)},status=HTTP_500_INTERNAL_SERVER_ERROR)

    