from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('change-password', views.change_password, name='changepassword'),
    path('login/forgot', views.forgot_password, name='forgot'),
    path('login/create-new-password/<token>',
         views.reset_password, name='change'),
]
