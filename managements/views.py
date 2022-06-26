from django.shortcuts import render
from django.views.generic import ListView

from complexes import models as complexes_models
from posts import models as posts_models
from questions import models as questions_models
from sales import models as sales_models


class HomeView(ListView):

    model = complexes_models.Complex
    paginate_by = 10
    ordering = "created_at"
    template_name = "manage/home.html"
    context_object_name = "complex_list"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["sale_list"] = sales_models.Sale.objects.all().order_by("created_at")[
            :10
        ]
        context["post_list"] = posts_models.Post.objects.all().order_by("created_at")[
            :10
        ]
        context["question_list"] = questions_models.Question.objects.all().order_by(
            "created_at"
        )[:10]

        return context
