from django.urls import path, include

urlpatterns = [
    path('tickets/', include('dashboard.Ticketing.urls')),
    path('notifications/', include('dashboard.Notification.urls')),
    path('feedbacks/', include('dashboard.Feedback.urls')),
]
