from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    UserSerializer,
    UserSerializerWithToken,
    MyTokenObtainPairSerializer
)


# Create your views here.

@api_view(['GET'])
def get_routes(request):
    routes = [
        '/api/v1/products',
        '/api/v1/products/<id>',
        '/api/v1/products/create',
        '/api/v1/products/delete/<id>',
        '/api/v1/products/<update>/<id>',
        '/api/v1/products/upload',
        '/api/v1/products/<id>/reviews',
        '/api/v1/products/top',
    ]
    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def register_user(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        data = {'message': 'User with this email already exists'}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user = request.user
    serializer = UserSerializerWithToken(user, many=False)

    data = request.data
    user.first_name = data['name']
    user.username = data['email']
    user.email = data['email']

    if data['password'] != '':
        user.password = make_password(data['password'])

    user.save()
    return Response(serializer.data)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
