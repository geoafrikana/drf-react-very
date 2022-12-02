from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission, DjangoModelPermissions,SAFE_METHODS


class PostUserWritePermission(BasePermission):
    message = 'Only the author can edit'
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            print(SAFE_METHODS)
            return True
        return obj.author == request.user


class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer