from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, default='')
    birth_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'author'
        ordering = ['name']

    def __str__(self):
        return self.name