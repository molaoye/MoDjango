from rest_framework import serializers
from web_app.models import *


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'news_class', 'date', 'show', 'content')