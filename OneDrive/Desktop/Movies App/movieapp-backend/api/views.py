from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Movie, UserMovie
from .serializers import MovieSerializer, UserMovieSerializer
import requests

class MovieList(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

class MovieDetail(APIView):
    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

class UserMovieList(APIView):
    def get(self, request):
        user_movies = UserMovie.objects.filter(user=request.user)
        serializer = UserMovieSerializer(user_movies, many=True)
        return Response(serializer.data)

class UserMovieDetail(APIView):
    def get(self, request, pk):
        user_movie = UserMovie.objects.get(pk=pk)
        serializer = UserMovieSerializer(user_movie)
        return Response(serializer.data)

class AddMovie(APIView):
    def post(self, request):
        tmdb_id = request.data['tmdb_id']
        response = requests.get(f'https://api.themoviedb.org/3/movie/{tmdb_id}?api_key=516e4036f09dd63e6f0d8408f80d65b0')
        data = response.json()
        movie, created = Movie.objects.get_or_create(tmdb_id=tmdb_id, defaults={'title': data['title'], 'overview': data['overview'], 'poster_path': data['poster_path']})
        user_movie = UserMovie.objects.create(user=request.user, movie=movie, rank=request.data['rank'])
        serializer = UserMovieSerializer(user_movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)