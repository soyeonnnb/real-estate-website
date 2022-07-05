from django.shortcuts import render, redirect
from django.views.generic import View, DetailView, UpdateView
from django.core.paginator import Paginator
from django.urls import resolve, reverse, reverse_lazy
from django.db.models import Q

from . import models
from . import forms


class SaleHomeView(View):
    def get(self, request):
        current_url = resolve(request.path_info)
        if current_url.app_names[0] == "managements":
            template_name = "manage/sale_list.html"
        else:
            template_name = "sales/sale_list.html"
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
                if current_url.app_names[0] == "sales":
                    filter_args["is_sold"] = False
                qs = models.Sale.objects.filter(**filter_args)
                if q is not None:
                    qs = qs.filter(q).order_by("-pk")
                paginator = Paginator(qs, 10, orphans=4)
                page = request.GET.get("page", 1)
                sales = paginator.get_page(page)

                return render(
                    request,
                    template_name,
                    {"form": form, "sales": sales},
                )
        else:
            form = forms.SearchForm()
            if current_url.app_names[0] == "sales":
                sales_list = models.Sale.objects.filter(is_sold=False).order_by("-pk")
            else:
                sales_list = models.Sale.objects.order_by("-pk")
            paginator = Paginator(sales_list, 10, orphans=4)
            page = request.GET.get("page", 1)
            sales = paginator.get_page(page)
        return render(
            request,
            template_name,
            {"form": form, "sales": sales},
        )


class SaleDetailView(DetailView):

    model = models.Sale
    content_object_name = "sale"


class SaleUpdateView(UpdateView):

    model = models.Sale
    form_class = forms.SaleForm

    def get_context_data(self, *args, **kwargs):
        context = super(SaleUpdateView, self).get_context_data(*args, **kwargs)
        context["page_title"] = "매물 수정"
        return context

    def get_success_url(self):
        return reverse_lazy("sales:detail", kwargs={"pk": self.object.pk})
