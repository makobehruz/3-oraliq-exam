from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('list/', views.post_list, name='list'),
    path('contact/', views.contact_list, name='contact'),
    path('approved/', views.contact_approved, name='approved'),
    path('create/', views.post_create, name='create'),
    path('detail/<int:pk>/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='detail'),
    path('about/', views.about_list, name='about'),
    path('search/', views.blog_search, name='blog_search'),
]