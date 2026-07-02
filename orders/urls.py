from django.urls import path
from . import views

urlpatterns = [
    path("place/", views.place_order, name="place_order"),
    path("success/", views.order_success, name="order_success"),
    path("history/", views.order_history, name="order_history"),
]