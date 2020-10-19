from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from .models import Author, News
from .serializers import NewsSerializer, AuthorSerializer

class NewsList(APIView):
    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

class AuthorList(APIView):
    def get(self, request, format=None):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def api_data(request, format=None):
    return Response({
        'authors': reverse('authors-list', request=request, format=format),
        'news': reverse('news-list', request=request, format=format)
    })



