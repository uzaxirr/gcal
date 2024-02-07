from django.contrib import admin
from django.urls import path

from mycalendar.views import EventView, UserEventsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/<int:event_id>/', EventView.as_view(), name='event-detail'),
    path('events/', EventView.as_view(), name='event-list'),
    path('events/user/<int:user_id>/', UserEventsView.as_view(), name='user-events'),
]
