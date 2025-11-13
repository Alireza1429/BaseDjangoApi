from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('send-broadcast/', views.BroadcastNotificationAPIView.as_view(), name='send-broadcast-notification'),
]