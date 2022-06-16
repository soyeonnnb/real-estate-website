from django.contrib import admin
from . import models


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):

    """Question Admin"""

    list_display = (
        "title",
        "phone",
        "secret",
        "is_answered",
    )
    list_filter = (
        "secret",
        "is_answered",
    )


@admin.register(models.QuestionImage)
class QuestionImageAdmin(admin.ModelAdmin):

    """Question Image Admin"""

    list_display = ("question",)


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):

    """Answer Admin"""

    list_display = (
        "question",
        "title",
    )
