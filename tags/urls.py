from django.urls import path
from . import views


app_name = 'tags'

urlpatterns = [
    path('list/', views.tag_list, name='list'),
    path('create/', views.tag_create, name='create'),
    path('delete/<int:pk>/', views.tag_delete, name='delete'),
]