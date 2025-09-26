from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path("room/", views.chat_room, name="chat_room"),
    path("delete/<int:labour_id>/<int:customer_id>/", views.delete_chat, name="delete_chat"),
]
