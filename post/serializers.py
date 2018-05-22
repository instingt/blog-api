from rest_framework import serializers

from core.models import Post, Image


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'url_slug', 'body', 'is_published')


class ImageSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass  # dummy

    name = serializers.CharField()
    image = serializers.ImageField(use_url=False)

    def create(self, validated_data):
        return Image.objects.create(**validated_data)
