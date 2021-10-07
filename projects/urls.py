from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("cart/<str:title>", views.project_detail, name="project_detail"),
    path("show_cart", views.show_cart, name="show_cart"),
    path("delete/<str:title>", views.delete, name="delete"),
]