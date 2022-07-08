from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponseRedirect

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


def question_create_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        text = request.POST.get("text")
        question = models.Question.objects.create(name=name, phone=phone, text=text)
        question.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
