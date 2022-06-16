from django.db import models
from core.models import TimeStampedModel
import random


class Question(TimeStampedModel):

    """Question Model"""

    title = models.CharField(max_length=150)
    phone = models.CharField(max_length=12)
    secret = models.BooleanField(default=False)
    text = models.TextField()
    is_answered = models.BooleanField()


def question_directory_path(instance, filename):
    n = random.randint(10000, 99999)
    return f"question/question_{instance.id}/{filename}-{n}"


class QuestionImage(TimeStampedModel):

    """Question Image Model"""

    question = models.ForeignKey(
        Question, related_name="question_image", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to=question_directory_path)


class Answer(TimeStampedModel):

    """Answer Model"""

    question = models.ForeignKey(
        Question, related_name="answer", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
