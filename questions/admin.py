from django.contrib import admin
from . import models


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):

    """Question Admin"""

    list_display = ("name", "phone", "is_answered", "created_at")
    list_filter = ("is_answered",)
