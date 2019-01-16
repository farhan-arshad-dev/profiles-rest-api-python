from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    def get(self, request, format=None):
        """Retuns a list of APIView feature."""

        hello_apiview = [
            'Uses HTTp methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', "hello_apiview": hello_apiview})
