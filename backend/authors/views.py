from django.shortcuts import render

# Create your views here.
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets
from .models import Author
from .serializers import AuthorSerializer


@extend_schema_view(
    list=extend_schema(tags=['Authors']),
    retrieve=extend_schema(tags=['Authors']),
    create=extend_schema(tags=['Authors']),
    update=extend_schema(tags=['Authors']),
    partial_update=extend_schema(tags=['Authors']),
    destroy=extend_schema(tags=['Authors']),
)
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer