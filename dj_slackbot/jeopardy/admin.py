from django.contrib import admin

from .models import Clue, Category, Turn


admin.site.register(Clue)
admin.site.register(Category)
admin.site.register(Turn)
