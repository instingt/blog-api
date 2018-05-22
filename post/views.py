from rest_framework import generics, mixins

from core.models import Post, Image
from post.serializers import PostSerializer, ImageSerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ImageCreate(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
