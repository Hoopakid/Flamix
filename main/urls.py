from django.urls import path
from .views import HomeTemplateView, BlogTemplateView, blog_single, ContactTemplateView, ServicesView, \
    ShoppingCartTemplateView, \
    IncrementCountAPIView, DecrementCountAPIView, ChangeCountAPIView, CommentView, quality_printing, \
    ontime_delivery, money_back_guarantee, support, AddProductView, OrderTemplateView, ComboShoppingCartTemplateView, \
    UserJoinTeamTemplateView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('shopping-cart', ShoppingCartTemplateView.as_view(), name='shopping-cart'),
    path('services', ServicesView.as_view(), name='services'),
    path('add-product', AddProductView.as_view(), name='add_product'),
    path('comment', CommentView.as_view(), name='comment'),
    path('checkout', OrderTemplateView.as_view(), name='checkout'),
    path('combo', ComboShoppingCartTemplateView.as_view(), name='combo'),
    path('contact', ContactTemplateView.as_view(), name='contact'),
    path('add-team', UserJoinTeamTemplateView.as_view(), name='team'),
    path('blog', BlogTemplateView.as_view(), name='blog'),
    path('blog-single', blog_single, name='blog-single'),
    path('services/quality-printing', quality_printing, name='quality-printing'),
    path('services/ontime-delivery', ontime_delivery, name='ontime-delivery'),
    path('services/money-back-guarantee', money_back_guarantee, name='money-back-guarantee'),
    path('services/support', support, name='support'),

    # API
    path('increment', csrf_exempt(IncrementCountAPIView.as_view()), name='increment'),
    path('decrement', csrf_exempt(DecrementCountAPIView.as_view()), name='decrement'),
    path('change', csrf_exempt(ChangeCountAPIView.as_view()), name='change'),
]

# ORM - Object Relational Mapping
