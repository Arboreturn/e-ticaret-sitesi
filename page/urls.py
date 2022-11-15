from django.urls import path
from .views import (
    # Manage:
    manage_list,
    
    # Page:
    page_list,
    
    # Carousel:
    carousel_create,
    carousel_list,
    carousel_update,              
)


urlpatterns = [
    path('',manage_list,name="manage_list"),
    
    # Carousel: 
    path('carousel_list/',carousel_list,name="carousel_list"),
    path('carousel_create/',carousel_create,name="carousel_create"),
    path('carousel_update/<int:pk>/',carousel_update,name="carousel_update"),
    
    # Page:
    path('page/list/',page_list,name="page_list"),
]

