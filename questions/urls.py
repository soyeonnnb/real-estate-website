from django.urls import path
from . import views

app_name = "questions"

urlpatterns = [
    path("list/", views.QuestionListView.as_view(), name="list"),
    path("create/", views.question_create_view, name="create"),
    path("<int:pk>/detail/", views.QuestionDetailView.as_view(), name="detail"),
]
