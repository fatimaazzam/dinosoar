from django.urls import path
from .views import show_dino

app_name = "dinofacts"
urlpatterns = [
    path("show_dino/<str:name>", show_dino, name="show_dino"),


    ]