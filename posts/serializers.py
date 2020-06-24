from rest_framework.serializers import HyperlinkedModelSerializer
from posts.models import GhostPost

class GhostPostSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = GhostPost
        fields = (
            'boast_or_roast',
            'post',
            'up_votes',
            'down_votes',
            'total_votes',
            'submission_time'
        )
