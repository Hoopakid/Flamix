from django.urls import path
from .views import HomeTemplateView, blog, blog_single, contact, services

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('blog', blog, name='blog'),
    path('blog-single', blog_single, name='blog-single'),
    path('contact', contact, name='contact'),
    path('services', services, name='services'),
]
