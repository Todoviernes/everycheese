from django.urls import path

from everycheese.cheeses.views import CheeseListView, CheeseDetailView
app_name = "cheeses"

urlpatterns = [
    path(
        route='',
        view=CheeseListView.as_view(),
        name='list'
    ),
    path(
        route='<str:slug>/',
        view=CheeseDetailView.as_view(),
        name='detail'
    )
]
