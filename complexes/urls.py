from django.urls import path
from . import views

app_name = "complexes"

urlpatterns = [
    path("list/", views.ComplexListView.as_view(), name="list"),
    path("<int:pk>/detail/", views.ComplexDetailView.as_view(), name="detail"),
]
