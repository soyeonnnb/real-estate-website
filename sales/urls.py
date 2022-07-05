from django.urls import path
from . import views

app_name = "sales"

urlpatterns = [
    path("list/", views.SaleHomeView.as_view(), name="list"),
    path("create/", views.SaleCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", views.SaleDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", views.SaleUpdateView.as_view(), name="update"),
]
