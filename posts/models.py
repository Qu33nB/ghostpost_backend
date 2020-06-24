from django.db import models
from django.utils import timezone

# Create your models here.
class GhostPost(models.Model):
    boast_or_roast = models.BooleanField(default=False, help_text='Check box to make it a roast!')
    post = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0, blank=True, null=True, editable=False)
    down_votes = models.IntegerField(default=0, blank=True, null=True, editable=False)
    total_votes = models.IntegerField(default=0, blank=True, null=True, editable=False)
    submission_time = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.post
