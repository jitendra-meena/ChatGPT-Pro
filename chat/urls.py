from django.urls import path
from .views import home, user_login, dashboard, logout_user, register

urlpatterns = [
    path('', home, name='home'),
    path('register', register, name = 'register'),
    path('login', user_login, name = 'login'),
    path('logout', logout_user, name = 'logout'),

    path('dashboard/',dashboard,name='dashboard')

]