from django.conf.urls import include, url
from posts.views import GhostPostViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'ghostpost', GhostPostViewSet, basename='ghostpost')

urlpatterns = [
    url(r'^api/', include(router.urls))
]
