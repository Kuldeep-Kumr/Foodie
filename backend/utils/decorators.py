from functools import wraps
from django.http import JsonResponse
from rest_framework.authtoken.models import Token

def isOwner(view_func):
    @wraps(view_func)
    def _wrapped_view(viewset, request,*args,**kwargs):

        if 'HTTP_AUTHORIZATION' not in request.META:
            return JsonResponse({'error': 'Authentication credentials were not provided'},status=401)
        
        auth_header = request.META['HTTP_AUTHORIZATION']
        try:
            token = auth_header.split()[1]
        except:
            return JsonResponse({'error': 'Invaild token format'},status=401)
        try:
            token_obj = Token.objects.get(key=token)
            user = token_obj.user
        except Token.DoesNotExist:
            return JsonResponse({'error': 'Invaild token'},status=401)
        

        if not user.is_owner:
            return JsonResponse({'error':'Permission denied only owner can access'},status=403)
        
        return view_func(viewset, request,*args,**kwargs)
    return _wrapped_view

def isUser(view_func):
    @wraps(view_func)
    def _wrapped_view(viewset, request,*args,**kwargs):

        if 'HTTP_AUTHORIZATION' not in request.META:
            return JsonResponse({'error': 'Authentication credentials were not provided'},status=401)
        
        auth_header = request.META['HTTP_AUTHORIZATION']
        try:
            token = auth_header.split()[1]
        except:
            return JsonResponse({'error': 'Invaild token format'},status=401)
        try:
            token_obj = Token.objects.get(key=token)
            user = token_obj.user
        except Token.DoesNotExist:
            return JsonResponse({'error': 'Invaild token'},status=401)
        

        if user.is_owner:
            return JsonResponse({'error':'Permission denied only user can access'},status=403)
        
        return view_func(viewset, request,*args,**kwargs)
    return _wrapped_view