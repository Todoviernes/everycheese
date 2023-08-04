from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from everycheese.cheeses.models import Cheese


class CheeseListView(ListView):
    model = Cheese
    paginate_by = 30
    template_name = "cheeses/cheese_list.html"
