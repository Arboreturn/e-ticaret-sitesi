from django.contrib import admin
from .models import Page
# Register your models here.

@admin.register(Page)
class PagesAdmin(admin.ModelAdmin):
    search_fields = ('name', "description") # arama motoru 
