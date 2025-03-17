from django.urls import path
from Capcha import views

urlpatterns = [
    path("", views.capcha, name="capcha"),

]