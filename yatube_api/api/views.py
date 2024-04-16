from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions

from api.serializers import PostSerializer, GroupSerializer, CommentSerializer
from posts.models import Post, Group, Comment


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        queryset = Comment.objects.filter(post_id=post.id)
        return queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        serializer.save(
            post_id=post_id,
            author_id=self.request.user.id
        )
