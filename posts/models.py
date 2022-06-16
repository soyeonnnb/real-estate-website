from django.db import models
from core.models import TimeStampedModel


class Post(TimeStampedModel):

    """Post Model"""

    title = models.CharField(max_length=100)
    text = models.TextField()
