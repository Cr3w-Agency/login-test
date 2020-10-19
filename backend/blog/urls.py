from django.urls import path, include
from .views import NewsList, AuthorList, api_data
from rest_framework import routers



urlpatterns = [
    path('news/', NewsList.as_view(), name='news-list'),
    path('authors/', AuthorList.as_view(), name='authors-list'),
    path('data/', api_data)
]