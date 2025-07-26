from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('add/', views.add_event, name='add_event'),
    path('attend/<int:event_id>/', views.mark_attended, name='mark_attended'),
]
