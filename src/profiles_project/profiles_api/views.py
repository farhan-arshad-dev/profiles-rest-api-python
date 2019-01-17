from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Retuns a list of APIView feature."""

        hello_apiview = [
            'Uses HTTp methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', "hello_apiview": hello_apiview})

    def post(sefl, request):
        """Creata a hellow message  with out name."""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response ({'message': message})
        else:
            return Response(
                serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """handles updating an object."""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request"""

        return Response({'method': 'patch'})

    def delete(self, resquest, pk=None):
        """Delete and object."""

        return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):

    """Test API ViewSet."""

    def list(self, request):
        """Return a Hello Message"""

        a_viewset = [
            'Uses actions (list, create, retieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provedes more functionality with less code'
        ]

        return Response({'message': 'Hello!', "a_viewset":a_viewset})
