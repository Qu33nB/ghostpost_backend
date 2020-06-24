from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from posts.serializers import GhostPostSerializer
from posts.models import GhostPost

class GhostPostViewSet(ModelViewSet):
    serializer_class = GhostPostSerializer
    basename = 'ghostpost'
    queryset = GhostPost.objects.all()

    @action(detail=True, methods=['get'])
    def add_like(self, request, pk=None):
        post = GhostPost.objects.get(pk=pk)
        post.up_votes += 1
        post.total_votes += 1
        post.save()
        return Response({'post': 'likes'})

    @action(detail=True, methods=['get'])
    def add_dislike(self, request, pk=None):
        post = GhostPost.objects.get(pk=pk)
        post.down_votes += 1
        post.total_votes -= 1
        post.save()
        return Response({'post': 'dislikes'})     
