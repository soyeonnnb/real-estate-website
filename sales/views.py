from django.shortcuts import render
from django.views.generic import ListView

from . import models


class SaleHomeView(ListView):

    model = models.Sale
    paginate_by = 10
    paginate_orphans = 2
    template_name = "sales/sale_list.html"
    context_object_name = "sales"
    ordering = "-pk"
