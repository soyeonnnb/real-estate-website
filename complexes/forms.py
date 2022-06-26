from django import forms
from django.forms import modelformset_factory

from . import models


class ComplexForm(forms.ModelForm):
    class Meta:
        model = models.Complex
        fields = (
            "category",
            "name",
            "parking",
            "heating",
            "approval_use",
            "company",
            "latitude",
            "longitude",
        )
        labels = {
            "category": "카테고리",
            "name": "단지명",
            "parking": "총 주차 대수",
            "heating": "난방 방식",
            "approval_use": "사용 승인일",
            "company": "회사",
            "latitude": "위도",
            "longitude": "경도",
        }


CreateComplexAreaFormset = modelformset_factory(
    models.ComplexArea,
    fields=(
        "supply_area",
        "exclusive_private_area",
        "room",
        "bath",
    ),
    labels={
        "supply_area": "공급면적",
        "exclusive_private_area": "전용면적",
        "room": "방 개수",
        "bath": "욕실 개수",
    },
)

CreateComplexSubFormset = modelformset_factory(
    models.ComplexSub,
    fields=(
        "building",
        "floor",
        "apartment",
        "facing",
        "latitude",
        "longitude",
    ),
    labels={
        "building": "동",
        "floor": "층",
        "apartment": "세대 수",
        "facing": "햇빛 방향",
        "latitude": "위도",
        "longitude": "경도",
    },
)
