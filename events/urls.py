from django.urls import path
from events import views


urlpatterns = [
    path('events/', views.events, name='events'),
    path('events/list/', views.EventListView.as_view(), name='event-list'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('event/create/', views.EventCreateView.as_view(), name='event-create'),
    path('event/update/<int:pk>', views.EventUpdateView.as_view(), name='event-update'),
    path('event/delete/<int:pk>', views.EventDeleteView.as_view(), name='event-delete'),
    path('event_users/', views.event_users, name='event_users'),
    path('add_users/', views.add_user, name='add_user'),
    path('add_event/', views.add_event, name='events'),
    path('add_event_users/', views.add_event_users, name='event_users')
]