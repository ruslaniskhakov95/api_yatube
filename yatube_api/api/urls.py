from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet


router = SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments'
)


urlpatterns = [
    path('', include(router.urls)),
]
