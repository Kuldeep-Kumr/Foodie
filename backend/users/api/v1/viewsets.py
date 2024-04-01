from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from restaurant.api.v1.serializers import RestaurantSerializer
from users.models import User
from users.api.v1.serializers import UserSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_200_OK,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_406_NOT_ACCEPTABLE
)

class UserViewSet(ModelViewSet):
    http_method_names=['post','delete']
    queryset=User.objects.all()
    serializer_class=UserSerializer
    def create(self, request):
        is_owner=False
        try:
            user=self.queryset.get(username=request.data['email'])
            return Response({"message":"User already added"},status=HTTP_200_OK)
        except:
            pass
        try:
            request.data['username']=request.data['email']
            request.data['password']=make_password(request.data['password'],None)
            serializer=self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                if serializer.data['is_owner']:
                    is_owner=True
                    request.data["user"]=serializer.data['id']
                    resturant_serializer=RestaurantSerializer(data=request.data)
                    if resturant_serializer.is_valid():
                        resturant_serializer.save()
                user=User.objects.get(username=serializer.data['username'])
                token,_ = Token.objects.get_or_create(user=user)
                return Response({"message":"User added successfully","token":str(token),"is_owner":is_owner},status=HTTP_201_CREATED)
            return Response({"message":serializer.error_messages},status=HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            return Response({"message":str(e)},status=HTTP_500_INTERNAL_SERVER_ERROR)
        
    def destroy(self, request, *args, **kwargs):
        result=get_object_or_404(Token, key=kwargs.get('pk'))
        try:
            result.delete()  
            return Response({"message:Logout Successfully"},status=HTTP_200_OK)
        except Exception as e:
            return Response({"message":result},status=HTTP_406_NOT_ACCEPTABLE)
    
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user=User.objects.filter(username=user)
        serializer=UserSerializer(user,many=True)
        return Response({
            'token': token.key,
            'is_owner':serializer.data[0]['is_owner']
        })