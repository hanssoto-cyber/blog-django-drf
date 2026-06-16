from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_list, name='articles_list'),
    path('authors/', views.authors_list, name='authors_list'),
    path('authors/create/', views.author_create, name='author_create'),
    path('articles/create/', views.article_create, name='article_create'),
]