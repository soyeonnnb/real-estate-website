from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator
from django.db.models import Q

from . import models
from . import forms


class SaleHomeView(View):
    def get(self, request):
        sale_type = request.GET.get("sale_type")
        if sale_type:
            form = forms.SearchForm(request.GET or None)
            if form.is_valid():
                sale_type = form.cleaned_data.get("sale_type")
                address = form.cleaned_data.get("address")
                price_from = form.cleaned_data.get("price_from")
                price_to = form.cleaned_data.get("price_to")
                date_from = form.cleaned_data.get("date_from")
                date_to = form.cleaned_data.get("date_to")
                filter_args = {}
                if sale_type:
                    filter_args["type__in"] = sale_type
                q = None
                if address:
                    q = Q()
                    for a in address:
                        q.add(Q(address__contains=a), q.OR)
                        q.add(
                            Q(complex_sub__complex_area__complex__address__contains=a),
                            q.OR,
                        )
                if price_from is not None:
                    filter_args["amount__gte"] = price_from
                if price_to is not None:
                    filter_args["amount__lte"] = price_to
                if date_from is not None:
                    filter_args["available_date__gte"] = date_from
                if date_to is not None:
                    filter_args["available_date__lte"] = date_to
                qs = models.Sale.objects.filter(**filter_args)
                if q is not None:
                    qs = qs.filter(q).order_by("-pk")
                paginator = Paginator(qs, 10, orphans=4)
                page = request.GET.get("page", 1)
                sales = paginator.get_page(page)
                return render(
                    request, "sales/sale_list.html", {"form": form, "sales": sales}
                )
        else:
            form = forms.SearchForm()
            sales_list = models.Sale.objects.order_by("-pk")
            paginator = Paginator(sales_list, 10, orphans=4)
            page = request.GET.get("page", 1)
            sales = paginator.get_page(page)
            print(sales_list)
        return render(request, "sales/sale_list.html", {"form": form, "sales": sales})
