from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from orders.api.v1.serializers import OrderSerializer,UserOrderSerializer
from restaurant.api.v1.serializers import RestaurantSerializer,MenuSerializer
from restaurant.models import Restaurant,Menu
from orders.models import Order
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_406_NOT_ACCEPTABLE,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from reviews.api.v1.serializers import UserReviewSerializer
from reviews.models import Review
from utils.decorators import isUser,isOwner
from utils.fetch_id import get_restaurant_id
from django.db.models import Avg


class RestaurantViewSet(ModelViewSet):
    http_method_names=['get']
    queryset=Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    @isUser
    def list(self, request,*args,**kwargs):
        try:
            queryset=self.queryset
            name = request.query_params.get('name', '')
            location = request.query_params.get('location', '')
            cuisine = request.query_params.get('cuisine', '')
            if location:
                queryset=queryset.filter(location__icontains=location).distinct()
            if cuisine:
                queryset=queryset.filter(cuisine__icontains=cuisine).distinct()
            if name:
                queryset=queryset.filter(name__icontains=name).distinct()
            if len(queryset)==0:
                return Response({"message":"Nothing Found"},status=HTTP_200_OK)
            queryset = queryset.annotate(avg_rating=Avg('review__rating'))
            serializer=self.serializer_class(queryset,many=True)
            try:
                return Response({"message":"Resturants","data":serializer.data},status=HTTP_200_OK)
            except:
                return Response({"message":serializer.error_messages},status=HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            return Response({"message":str(e)},status=HTTP_500_INTERNAL_SERVER_ERROR)
    @isUser
    def retrieve(self, request, *args, **kwargs):
        try:
            queryset=Menu.objects.filter(restaurant=kwargs.get('pk'))
            queryset = queryset.annotate(avg_rating=Avg('review__rating'))
            serializer=MenuSerializer(queryset,many=True)
            try:
                return Response({"message":"Menu","data":serializer.data},status=HTTP_200_OK)
            except:
                return Response({"message":serializer.error_messages},status=HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            return Response({"message":str(e)},status=HTTP_500_INTERNAL_SERVER_ERROR)

class RestaurantMenuViewSet(ModelViewSet):
    http_method_names=['get','post','patch','delete']
    queryset=Menu.objects.all()
    serializer_class = MenuSerializer
    @isOwner
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.queryset.filter(restaurant=get_restaurant_id(request))
            queryset = queryset.annotate(avg_rating=Avg('review__rating'))
            serializer = self.serializer_class(queryset,many=True)
            try:
                return Response({"message":"Menu","data":serializer.data},status=HTTP_200_OK)
            except:
                return Response({"message":serializer.error_messages,},status=HTTP_406_NOT_ACCEPTABLE)
            
        except Exception as e:
            return Response({"message":str(e)},status=HTTP_500_INTERNAL_SERVER_ERROR)
        
    @isOwner
    def retrieve(self, request, *args, **kwargs):
        try:
            queryset = Review.objects.filter(restaurant=get_restaurant_id(request),id=kwargs.get('pk'))
            serializer = UserReviewSerializer(queryset,many=True)
            try:
                return Response({"message":"Menu Reviews","data":serializer.data},status=HTTP_200_OK)
            except:
                return Response({"message":serializer.error_messages,"data":[]},status=HTTP_406_NOT_ACCEPTABLE)
            
        except Exception as e:
            return Response({"message":str(e)},status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    @isOwner
    def create(self,request, *args, **kwargs):
        try:
            request.data['restaurant']=get_restaurant_id(request)
            serializer=self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"Menu added successfully","data":serializer.data},status=HTTP_201_CREATED)
            return Response({"message":serializer.error_messages},status=HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            return Response({"message":str(e)},status=HTTP_500_INTERNAL_SERVER_ERROR)
    
    @isOwner
    def partial_update(self, request, *args, **kwargs):
        try:
            result,created = self.queryset.get_or_create(restaurant=get_restaurant_id(request), id=kwargs.get('pk'))
            if not created:
                serializer = self.serializer_class(result, data = request.data, partial=True)  
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message":"Menu updated successfully","data":serializer.data},status=HTTP_200_OK)
                return Response({"message":serializer.error_messages},status=HTTP_406_NOT_ACCEPTABLE)
            return Response({"message":"Dish does not exist","data":serializer.data},status=HTTP_201_CREATED)
        except Exception as e:
            return Response({"message":str(e)},status=HTTP_500_INTERNAL_SERVER_ERROR)
        
    @isOwner
    def destroy(self, request, *args, **kwargs):
        result = get_object_or_404(Menu, restaurant=get_restaurant_id(request), id=kwargs.get('pk'))
        try:
            result.delete()  
            return Response({"message":"Deleted successfully"},status=HTTP_200_OK)
        except Exception as e:
            return Response({"message":result,},status=HTTP_500_INTERNAL_SERVER_ERROR)
     
class OrderViewSet(ModelViewSet):
    http_method_names=['get','patch','delete']
    queryset=Order.objects.all()
    serializer_class = OrderSerializer
    @isOwner
    def list(self, request,*args,**kwargs):
        try:
            queryset = self.queryset.filter(restaurant=get_restaurant_id(request)).order_by('-id')
            serializer=UserOrderSerializer(queryset,many=True)
            print(serializer)
            if serializer.data:
                return Response({"message":"All Orders","data":serializer.data},status=HTTP_201_CREATED)
            return Response({"message":serializer.error_messages},status=HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            return Response({"message":str(e)},status=HTTP_500_INTERNAL_SERVER_ERROR)
        
    @isOwner
    def retrieve(self, request, *args, **kwargs):
        try:
            queryset = self.queryset.filter(restaurant=get_restaurant_id(request),id=kwargs.get("pk"))
            serializer=self.serializer_class(queryset,many=True)
            if serializer.data:
                return Response({"message":"Order detail","data":serializer.data},status=HTTP_201_CREATED)
            return Response({"message":serializer.error_messages},status=HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            return Response({"message":str(e)},status=HTTP_500_INTERNAL_SERVER_ERROR)
          
    @isOwner
    def partial_update(self, request,*args,**kwargs):
        try:
            result = self.queryset.get(restaurant=get_restaurant_id(request), id=kwargs.get("pk"))
            if result:
                serializer = self.serializer_class(result, data = request.data, partial=True) 
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message":"Order status updated successfully","data":serializer.data},status=HTTP_200_OK)
                return Response({"message":serializer.error_messages,"data":[]},status=HTTP_406_NOT_ACCEPTABLE)
            return Response({"message":"No such item exist"},status=HTTP_200_OK)
        except Exception as e:
            return Response({"message":str(e)},status=HTTP_500_INTERNAL_SERVER_ERROR)