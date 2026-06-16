from rest_framework import serializers
from .models import Article
from authors.models import Author
from authors.serializers import AuthorSerializer


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        source='author',
        queryset=Author.objects.all(),
        write_only=True,
    )

    class Meta:
        model = Article
        fields = [
            'id', 'title', 'content', 'status',
            'author', 'author_id',
            'published_at', 'created_at', 'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']