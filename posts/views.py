from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from posts.serializers import GhostPostSerializer
from posts.models import GhostPost

class GhostPostViewSet(ModelViewSet):
    serializer_class = GhostPostSerializer
    basename = 'ghostpost'
    queryset = GhostPost.objects.all()
