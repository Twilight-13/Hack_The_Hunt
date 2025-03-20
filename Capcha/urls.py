from django.urls import path
from Capcha import views

urlpatterns = [
    path("", views.capcha, name="capcha"),  # Display captcha form
    path("verify/", views.verify_captcha, name="verify_captcha"),  # Verification endpoint
]
