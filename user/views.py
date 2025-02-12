from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404


class UserListCreateView(APIView):
    def get(self, request):
        users = User.object.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(user, id = pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    def put(self, request, pk):
        data = request.data
        user = get_object_or_404(User, id = pk)
        serializer = UserSerializer(user, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)