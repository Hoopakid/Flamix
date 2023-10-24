from django.urls import path
from .views import HomeTemplateView, blog, blog_single, contact, services, ShoppingCartTemplateView, \
    IncrementCountAPIView, DecrementCountAPIView, ChangeCountAPIView, CommentView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('shopping-cart', ShoppingCartTemplateView.as_view(), name='shopping-cart'),
    path('comment', CommentView.as_view(), name='comment'),
    path('blog', blog, name='blog'),
    path('blog-single', blog_single, name='blog-single'),
    path('contact', contact, name='contact'),
    path('services', services, name='services'),

    # API
    path('increment', csrf_exempt(IncrementCountAPIView.as_view()), name='increment'),
    path('decrement', csrf_exempt(DecrementCountAPIView.as_view()), name='decrement'),
    path('change', csrf_exempt(ChangeCountAPIView.as_view()), name='change'),
]

# ORM - Object Relational Mapping
