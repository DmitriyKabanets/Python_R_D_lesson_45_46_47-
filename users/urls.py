from django.urls import path
from django.contrib.auth import views as auth_views

from users import views

urlpatterns = [
    path('hello/', views.user_hello_world, name='user_hello_world'),
    path('users/', views.users_list, name='users_list'),
    path('users/list/', views.UsersListView.as_view(), name='users-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]


