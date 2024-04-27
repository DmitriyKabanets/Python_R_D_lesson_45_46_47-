from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from users.models import User


def user_hello_world(request):
    return HttpResponse("<h2>Hello world</h2>")


def users_list(request):
    users = User.objects.all()
    users_number = len(users)

    return HttpResponse(f"<h1>Users count: {users_number}</h1>")


class UsersListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users_list'


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_detail_view.html'
    context_object_name = 'user_detail'

