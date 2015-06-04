from django.contrib.auth.models import User
from rest_framework import serializers
from ideas.models import Idea, IdeaComment
from userapp.models import UserProfile
from userapp.serializers import UserSerializer
from general.serializers import TagSerializer


class IdeaCommentSerializer(serializers.ModelSerializer):

    owner = UserSerializer(read_only=True)

    class Meta:
        model = IdeaComment
        fields = ('id', 'owner', 'timestamp', 'text', 'idea')
        read_only_fields = ('owner',)


class PostIdeaCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdeaComment
        fields = ('id', 'text')


class IdeaSerializer(serializers.ModelSerializer):
    modelslug = serializers.SlugField(read_only=True, source='slug')
    comments = IdeaCommentSerializer(many=True, read_only=True)
    # tags = TagSerializer(many=True, read_only=True)
    tags = serializers.StringRelatedField(many=True)
    owner = serializers.StringRelatedField()

    class Meta:
        model = Idea
        fields = ('id', 'owner', 'title', 'description', 'rating', 'modelslug', 'comments', 'tags')
        read_only_fields = ('owner',)

