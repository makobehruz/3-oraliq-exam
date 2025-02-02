from django.urls import path
from . import views


app_name = 'catalogs'

urlpatterns = [
    path('list/', views.category_list, name='list'),
    path('create/', views.category_create, name='create'),
    path('delete/<int:pk>/', views.category_delete, name='delete'),
]