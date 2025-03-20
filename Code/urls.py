from django.urls import path
from . import views

urlpatterns = [
    path('', views.decoder_view, name='decoder_view'),  # Home page with form
    path('decode_binary/', views.decoder_view, name='decode_binary') ,
    path('next_level/', views.next_level_view, name='next_level')# Handle binary decoding form submission
]
