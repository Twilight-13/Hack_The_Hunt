from django.urls import path
from Home import views

urlpatterns = [
    path("", views.login_view, name="landing"),


]