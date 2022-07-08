from django import forms

from . import models


class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = (
            "name",
            "phone",
            "text",
        )
