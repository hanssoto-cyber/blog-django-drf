from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer


@extend_schema_view(
    list=extend_schema(tags=['Articles']),
    retrieve=extend_schema(tags=['Articles']),
    create=extend_schema(tags=['Articles']),
    update=extend_schema(tags=['Articles']),
    partial_update=extend_schema(tags=['Articles']),
    destroy=extend_schema(tags=['Articles']),
)
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.select_related('author').order_by('-created_at')
    serializer_class = ArticleSerializer