from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    """Category Admin Definition"""

    list_display = ("name",)
    ordering = ("name",)


@admin.register(models.Complex)
class ComplexAdmin(admin.ModelAdmin):

    """Complex Admin Definition"""

    list_display = (
        "category",
        "name",
        "parking",
        "heating",
        "approval_use",
        "company",
    )
    list_filter = (
        "category",
        "heating",
    )


@admin.register(models.ComplexArea)
class ComplexAreaAdmin(admin.ModelAdmin):

    """Complex Area Admin Definition"""

    list_display = (
        "complex",
        "supply_area",
        "exclusive_private_area",
        "room",
        "bath",
    )
    list_filter = (
        "complex",
        "room",
        "bath",
    )


@admin.register(models.ComplexSub)
class ComplexSubAdmin(admin.ModelAdmin):

    """Complex Sub Admin Definition"""

    list_display = (
        "complex_area",
        "building",
        "floor",
        "apartment",
        "facing",
    )
    list_filter = ("facing",)


@admin.register(models.ComplexImage)
class ComplexImageAdmin(admin.ModelAdmin):

    """Complex Image Admin Definition"""

    list_display = ("complex",)
