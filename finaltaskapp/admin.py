from django.contrib import admin
from.models import Movies
# from .models import Category

# Register your models here.
admin.site.register(Movies)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name']
# admin.site.register(Category,CategoryAdmin)