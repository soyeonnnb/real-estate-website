from re import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse

from . import models
from . import forms


class CreateComplexView(CreateView):

    model = models.Complex
    form_class = forms.ComplexForm
    template_name = "complexes/complex_create.html"
    fields = [
        "category",
        "name",
        "parking",
        "heating",
        "approval_use",
        "company",
        "latitude",
        "longitude",
    ]

    def get_success_url(self):
        return reverse("core:home")


class ComplexListView(ListView):

    model = models.Complex
    template_name = "complexes/complex_list.html"
    paginate_by = 10
    paginate_orphans = 4
    context_object_name = "complexes"


class ComplexDetailView(DetailView):

    model = models.Complex
    context_object_name = "complex"
