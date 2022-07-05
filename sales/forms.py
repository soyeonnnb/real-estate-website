from django import forms
import datetime

from . import models
from complexes import models as complexes_models


class SearchForm(forms.Form):

    TYPE_SALE = "sale"
    TYPE_JEONSE = "jeonse"
    TYPE_MONTHLY = "monthly"
    TYPE_CHOICES = (
        (TYPE_SALE, "매매"),
        (TYPE_JEONSE, "전세"),
        (TYPE_MONTHLY, "월세"),
    )
    ADDRESS_EOMSA = "엄사"
    ADDRESS_GEUMAM = "금암"
    ADDRESS_DUMA = "두마"
    ADDRESS_CHOICES = (
        (ADDRESS_EOMSA, "엄사면"),
        (ADDRESS_GEUMAM, "금암동"),
        (ADDRESS_DUMA, "두마면"),
    )

    sale_type = forms.MultipleChoiceField(
        choices=TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "search-type-btn", "checked": ""}
        ),
        label="",
        required=True,
    )
    address = forms.MultipleChoiceField(
        choices=ADDRESS_CHOICES,
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "search-address-btn", "checked": ""}
        ),
        label="",
        required=True,
    )
    price_from = forms.IntegerField(label="", initial=0, min_value=0, required=False)
    price_to = forms.IntegerField(
        label="", initial=1000000000, min_value=0, required=False
    )
    date_from = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), label="", required=False
    )
    date_to = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), label="", required=False
    )


class SaleForm(forms.ModelForm):
    class Meta:
        model = models.Sale
        fields = (
            "type",
            "address",
            "deposit",
            "amount",
            "floor",
            "loan",
            "administrative_expense",
            "available_date",
            "description",
            "one_description",
            "is_sold",
        )
        widgets = {
            "deposit": forms.NumberInput(attrs={"min": 0}),
            "amount": forms.NumberInput(attrs={"min": 0}),
            "loan": forms.NumberInput(attrs={"min": 0}),
            "administrative_expense": forms.NumberInput(attrs={"min": 0}),
            "available_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super(SaleForm, self).__init__(*args, **kwargs)
        self.fields["category"] = forms.ModelChoiceField(
            queryset=complexes_models.Category.objects.all()
        )
        self.fields["complex"] = forms.ModelChoiceField(
            queryset=complexes_models.Complex.objects.all()
        )
        self.fields["complex_sub"] = forms.ModelChoiceField(
            queryset=complexes_models.ComplexSub.objects.all()
        )

    def save(self, *args, **kwargs):
        sale = super().save(commit=False)
        complex_sub = self.cleaned_data.get("complex_sub")
        sale.complex_sub = complex_sub
        sale.save()
