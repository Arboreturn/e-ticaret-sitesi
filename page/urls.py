from django.urls import path
from .page import views

urlpatterns = [
    path('manage/carousel_create',carousel_create),
]