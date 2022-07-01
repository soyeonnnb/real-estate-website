from django.urls import path

from . import views
from complexes import views as complexes_views
from posts import views as posts_views
from questions import views as questions_views
from sales import views as sales_views
from users import views as users_views

app_name = "managements"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path(
        "complexes/create_complex/",
        complexes_views.CreateComplexView.as_view(),
        name="create_complexes",
    ),
    path(
        "sales/sales_list/",
        sales_views.SaleHomeView.as_view(),
        name="sales_list",
    ),
]
