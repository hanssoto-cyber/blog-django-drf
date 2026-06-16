from django.urls import path, include

urlpatterns = [
    path('', include('authors.urls')),
    path('', include('articles.urls')),
]