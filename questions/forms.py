from django import forms

from . import models


class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = (
            "title",
            "phone",
            "secret_number",
            "text",
        )

    def save(self, *args, **kwargs):
        question = super().save(commit=False)
        secret_number = self.cleaned_data.get("secret_number")
        if secret_number is not None:
            question.secret = True
        question.save()
        return question
