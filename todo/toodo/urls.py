from django.urls import path
from . import views

app_name = 'toodo'
urlpatterns = [
    path('', views.index, name='home'),
    path('update_task/<pk>/', views.update_task, name='update'),
    path('delete_task/<pk>/', views.delete_task, name='delete'),
]
