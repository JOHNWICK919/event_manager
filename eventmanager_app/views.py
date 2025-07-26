from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Event
from .forms import EventForm

def event_list(request):
    filter_type = request.GET.get('filter', 'all')
    today = timezone.now().date()

    if filter_type == 'day':
        events = Event.objects.filter(date=today)
    elif filter_type == 'week':
        end_week = today + timedelta(days=7)
        events = Event.objects.filter(date__range=[today, end_week])
    elif filter_type == 'month':
        end_month = today + timedelta(days=30)
        events = Event.objects.filter(date__range=[today, end_month])
    else:
        events = Event.objects.all().order_by('date')

    return render(request, 'eventmanager_app/event_list.html', {
        'events': events,
        'filter_type': filter_type
    })

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'eventmanager_app/add_event.html', {'form': form})

def mark_attended(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.is_attended = True
    event.save()
    return redirect('event_list')
