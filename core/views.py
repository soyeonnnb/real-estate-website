from django.shortcuts import render
from django.views.generic import ListView

from complexes import models as complexes_models
from sales import models as sales_models

# Create your views here.
class HomeView(ListView):

    model = sales_models.Sale
    ordering = "created_at"
    context_object_name = "sales"
    paginate_by = 12
    paginate_orphans = 2
    template_name = "home.html"
