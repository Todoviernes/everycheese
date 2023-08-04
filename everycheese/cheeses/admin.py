from django.contrib import admin

# Register your models here.
from everycheese.cheeses.models import Cheese


@admin.register(Cheese)
class CheeseAdmin(admin.ModelAdmin):
    list_display = ("name", "firmness", "created", "modified")
