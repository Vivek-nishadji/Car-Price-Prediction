from django.contrib import admin
from django.urls import path
from prediction import views

urlpatterns = [
    path("", views.index, name="home"),
    path("predict", views.predict, name="predict"),
    path("chatbot", views.chatbot_page, name="chatbot"),  # <-- Added chatbot page URL
]