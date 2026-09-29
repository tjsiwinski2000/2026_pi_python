from django.urls import path
from . import views

app_name = "chatbot"

urlpatterns = [
    path("save-location/", views.save_location, name="save_location"),
    path('chat-reply/', views.chat_reply, name="chat_reply")
]