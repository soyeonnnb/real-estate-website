from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView
from django.urls import reverse

from . import models
from . import forms


class CreateComplexView(CreateView):

    model = models.Complex
    form_class = forms.ComplexForm
    template_name = "complexes/create_complex.html"
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
