from rest_framework import serializers
from .models import Movie, UserMovie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview', 'poster_path', 'tmdb_id')

class UserMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMovie
        fields = ('id', 'user', 'movie', 'rank')