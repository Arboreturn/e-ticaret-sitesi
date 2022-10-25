from django.contrib import admin
from .models import Page
# Register your models here.
    
class PageModify(admin.ModelAdmin):
    prepopulated_fields ={"slug":("title",)}
    list_display = ("pk","title","slug","status","updated_at",)
    list_filter = ("status",)
    list_editable = ("title","status")

admin.site.register(Page,PageModify)
    

# Django Structure
#-----------------
# M DB yapısı
# V View / Control
# T Template
# A admin
# F Forms
# Messages
# S Session