from django.db import models
from core.models import TimeStampedModel
import random


class Question(TimeStampedModel):

    """Question Model"""

    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    text = models.TextField()
    is_answered = models.BooleanField(default=False)
