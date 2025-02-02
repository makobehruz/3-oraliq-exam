from django.urls import path
from . import views


app_name ='authors'

urlpatterns = [
    path('list/', views.author_list, name='list'),
    path('create/', views.author_create, name='create'),
    path('delete/<int:pk>/', views.author_delete, name='delete'),

]