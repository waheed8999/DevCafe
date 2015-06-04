from django.contrib.auth.models import User
from ideas.serializers import IdeaSerializer, IdeaCommentSerializer, PostIdeaCommentSerializer
from ideas.models import Idea, IdeaComment
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from ideas.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import status


class IdeaList(generics.ListCreateAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class IdeaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,)


class IdeaCommentList(generics.ListAPIView):
    queryset = IdeaComment.objects.all()
    serializer_class = IdeaCommentSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class IdeaCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IdeaComment.objects.all()
    serializer_class = IdeaCommentSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,)


class AddComment(APIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, pk):
        idea = Idea.objects.get(id=pk)
        comment = PostIdeaCommentSerializer(data=request.data)
        if comment.is_valid():
            # comment.object.idea = idea
            # comment.object.owner = request.user
            comment.save(idea=idea, owner=request.user)
            return Response(comment.data, status=status.HTTP_201_CREATED)
        return Response(comment.errors, status=status.HTTP_400_BAD_REQUEST)
        # comment = IdeaComment.objects.create(text=request.data, owner=request.user, idea=idea)
        # comment.save()

        # return Response(IdeaCommentSerializer(comment), status=status.HTTP_201_CREATED)