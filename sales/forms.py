from django import forms
import datetime


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
