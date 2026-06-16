from rest_framework.routers import DefaultRouter
from authors.views import AuthorViewSet
from articles.views import ArticleViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='authors')
router.register(r'articles', ArticleViewSet, basename='articles')

urlpatterns = router.urls