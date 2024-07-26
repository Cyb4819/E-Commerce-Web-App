from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieList.as_view()),
    path('movies/<int:pk>/', views.MovieDetail.as_view()),
    path('user/movies/', views.UserMovieList.as_view()),
    path('user/movies/<int:pk>/', views.UserMovieDetail.as_view()),
    path('add/movie/', views.AddMovie.as_view()),
]