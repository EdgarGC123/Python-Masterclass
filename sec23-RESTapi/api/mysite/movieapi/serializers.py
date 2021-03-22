from myapp.models import Movie
from rest_framework import serializers
#the purpose of this file is to convert any db object (or many objects) into json format based on a particular model

class MovieSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Movie
        fields = ('name', 'description', 'rating', 'image')