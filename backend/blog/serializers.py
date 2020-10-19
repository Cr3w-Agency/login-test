from rest_framework import serializers
from .models import Author, News

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    news = NewsSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['user', 'created', 'news']