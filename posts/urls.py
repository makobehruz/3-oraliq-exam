from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('list/', views.post_list, name='list'),
    path('contact/', views.contact_list, name='contact'),
    path('create/', views.post_create, name='create'),
    path('detail/<int:pk>/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='detail'),
]