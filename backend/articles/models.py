from django.db import models
from authors.models import Author


class Article(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'draft', 'Borrador'
        PUBLISHED = 'published', 'Publicado'

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='articles',
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT,
    )
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'article'
        ordering = ['-created_at']

    def __str__(self):
        return self.title