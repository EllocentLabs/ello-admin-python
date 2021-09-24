from django.urls import path

from . import views

urlpatterns = [
    path('', views.ClientsList.as_view(), name='clients'),
    path('add', views.ClientAdd.as_view(), name='add-clients'),
    path('update/<int:pk>', views.ClientUpdate.as_view(), name='update-clients'),
    path('delete/<int:pk>', views.clientdel, name='delete-clients'),
    path('status/<int:pk>', views.changeStatus, name='change-status'),
]
