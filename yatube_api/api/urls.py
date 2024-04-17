from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views

from .views import PostViewSet, GroupViewSet, CommentViewSet


router_api_v1 = SimpleRouter()
router_api_v1.register(r'posts', PostViewSet)
router_api_v1.register(r'groups', GroupViewSet)
router_api_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments'
)


urlpatterns = [
    path('', include(router_api_v1.urls)),
    path('api-token-auth/', views.obtain_auth_token)
]
