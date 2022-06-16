from django.contrib import admin
from . import models


@admin.register(models.Sale)
class SaleAdmin(admin.ModelAdmin):

    """Sale Admin"""

    list_display = (
        "complex_sub",
        "type",
        "deposit",
        "amount",
        "available_date",
        "is_sold",
    )
    list_filter = (
        "type",
        "is_sold",
    )


@admin.register(models.SaleImage)
class SaleImageAdmin(admin.ModelAdmin):

    """Sale Image Admin"""

    list_display = ("sale",)
