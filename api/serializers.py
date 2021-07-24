from rest_framework import serializers
from . import models 


class RecommenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Album
        fields = ('title', 'artist', 'genre')