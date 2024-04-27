from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from events.models import Event, EventsUser
from users.models import User


def events(request):
    even = Event.objects.all()
    events_number = len(even)

    return HttpResponse(f"<h1>Events count: {events_number}</h1>")


class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events_list'


class EventCreateView(CreateView):
    model = Event
    fields = ['title', 'description', 'created_by']
    template_name = 'events/event_form.html'
    success_url = '/events/list/'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()
        ctx['title'] = 'Create Event'
        return ctx


class EventUpdateView(UpdateView):
    model = Event
    fields = ['title', 'description', 'created_by']
    template_name = 'events/event_form.html'
    success_url = '/events/list/'


class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('event-list')


class EventDetailView(DetailView):
    model = Event
    template_name = 'events/detail_view.html'
    context_object_name = 'detail_view'


def event_users(request):
    even_users = EventsUser.objects.all()
    even_users = len(even_users)

    return HttpResponse(f"<h1>Event Users count: {even_users}</h1>")


def add_user(request):
    new_user = User(first_name='First', last_name='FFFFFFFF', username='first')
    new_user_second = User(first_name='Second', last_name='Ssss', username='second')
    new_user_third = User(first_name='Third', last_name='Tttttt', username='third')
    new_user_fourth = User(first_name='Fourth', last_name='Ff', username='fourth')
    new_user.save()
    new_user_second.save()
    new_user_third.save()
    new_user_fourth.save()
    return HttpResponse("<h3>Ok</h3>")


def add_event(request):
    new_event = Event(title='some title some title some title', description='description description', created_by_id=3, begin_at="2023-01-01", end_at="2024-03-03", max_users=600, is_active=True)
    new_event.save()
    return HttpResponse("<h3>Ok</h3>")


def add_event_users(request):
    new_event_users = EventsUser(user_id_id=1, event_id_id=1, created_at="2023-01-01", score=100)
    new_event_users.save()
    return HttpResponse("<h3>Add event users - Ok</h3>")

