from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from . import models
from . import forms

# Create your views here.
class QuestionListView(ListView):

    model = models.Question
    paginate_by = 10
    paginate_orphans = 4
    context_object_name = "questions"
    ordering = "-pk"


class QuestionDetailView(DetailView):

    model = models.Question


class QuestionCreateView(CreateView):

    model = models.Question
    form_class = forms.QuestionCreateForm
    template_name = "questions/question_create.html"

    def get_success_url(self):
        return reverse("questions:detail", kwargs={"pk": self.object.pk})
