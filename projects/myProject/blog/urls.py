from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name= 'single-blog'),
    path('mm/', views.blog, name= 'blog'),
    path('elements', views.elements, name= 'elements'),
    path('contact' , views.contact, name= 'contact'),
    path('menu' , views.contact, name= 'menu'),
]