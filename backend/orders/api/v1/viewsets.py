from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from orders.models import Order
from orders.api.v1.serializers import OrderSerializer,UserOrderSerializer
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_406_NOT_ACCEPTABLE,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from restaurant.api.v1.serializers import MenuSerializer
from restaurant.models import Menu
from utils.decorators import isUser
from utils.fetch_id import get_user_id
    
class OrderViewSet(ModelViewSet):
    http_method_names=['get','post','delete']
    queryset=Order.objects.all()
    serializer_class = UserOrderSerializer
    @isUser
    def list(self, request,*args,**kwargs):
        try:
            queryset = self.queryset.filter(user=get_user_id(request)).order_by('-id')
            serializer=self.serializer_class(queryset,many=True)
            try:
                return Response({"message":"All Orders","data":serializer.data},status=HTTP_200_OK)
            except:
                return Response({"message":serializer.error_messages},status=HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            return Response({"message":str(e)},status=HTTP_500_INTERNAL_SERVER_ERROR)
    @isUser
    def create(self, request,*args,**kwargs):
        try:
            if 'quantity' not in request.data:
                request.data['quantity']=1
            queryset = Menu.objects.filter(id=request.data['menu'])
            menu_serializer = MenuSerializer(queryset,many=True)
            if menu_serializer.data:
                request.data['price']=menu_serializer.data[0]['price']*request.data['quantity']
                request.data['user']=get_user_id(request)
                request.data['status']="placed"
                request.data['restaurant']=menu_serializer.data[0]['restaurant']
                serializer=OrderSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message":"Order placed successfully","data":serializer.data},status=HTTP_201_CREATED)
            return Response({"message":serializer.error_messages},status=HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            return Response({"message":str(e)},status=HTTP_500_INTERNAL_SERVER_ERROR)
        
    @isUser
    def destroy(self, request,*args,**kwargs):
        try:
            result = get_object_or_404(Order, user=get_user_id(request), id=kwargs.get('pk'))
            result.delete()  
            return Response({"message":"Deleted successfully"},status=HTTP_200_OK)
        except Exception as e:
            return Response({"message":result},status=HTTP_500_INTERNAL_SERVER_ERROR)