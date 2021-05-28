from django.urls import path
from rest_framework.generics import UpdateAPIView
from .views import GetRoom, JoinRoom, RoomView, CreateRoomView, UpdateRoom, UserinRoom, LeaveRoom

urlpatterns = [
    path('room',RoomView.as_view()),
    path('create-room', CreateRoomView.as_view()),
    path('get-room', GetRoom.as_view()),
    path('join-room', JoinRoom.as_view()),
    path('user-in-room', UserinRoom.as_view()),
    path('leave-room', LeaveRoom.as_view()),
    path('update-room', UpdateRoom.as_view())
]
