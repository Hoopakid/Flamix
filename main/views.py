import json

from django.shortcuts import render, redirect
from .models import ShoppingCart, Image, Products
from django.views import View
from django.db.models import Q
from django.contrib import messages
from django.http.response import JsonResponse


class HomeTemplateView(View):
    template_name = 'index.html'
    context = {}

    def get(self, request):
        service_data = Products.objects.all()
        services_data = []
        for service in service_data:
            image = Image.objects.filter(service=service).first()
            service.image = image
            services_data.append(service)
        self.context.update({'service_data': services_data})
        return render(request, self.template_name, self.context)

    def post(self, request):
        service_id = request.POST.get('service_id')
        user = request.user
        if not ShoppingCart.objects.filter(Q(user=user) & Q(service_id=service_id)).exists():
            shopping_cart = ShoppingCart.objects.create(
                user=user, service_id=service_id
            )
            shopping_cart.save()
            messages.info(request, 'Product added successfully !!!')
            return redirect(f'/#service_{service_id}')

        messages.error(request, 'This service already exists in cart')
        return redirect(f'/#service_{service_id}')


class ShoppingCartTemplateView(View):
    template_name = 'shopping_cart.html'
    context = {}

    def get(self, request):
        if request.user.id is None:
            return redirect('/accounts/login')
        shopping_cart = ShoppingCart.objects.filter(user=request.user)
        data = []
        for index, value in enumerate(shopping_cart):
            image = Image.objects.filter(service=value.service).first()
            value.img = image
            value.index = index + 1
            data.append(value)
        self.context.update({'shopping_cart_products': data})
        return render(request, self.template_name, self.context)

    def post(self, request):
        shopping_cart_id = request.POST.get('shopping_cart_id')
        ShoppingCart.objects.get(pk=shopping_cart_id).delete()
        return redirect('/shopping-cart')


class IncrementCountAPIView(View):

    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            shopping_cart_id = json_data.get('id')
            shopping_cart = ShoppingCart.objects.get(pk=shopping_cart_id)
            shopping_cart.count += 1
            shopping_cart.save()
        except Exception as e:
            return JsonResponse({'success': False, 'error': e})
        return JsonResponse({'success': True})


class DecrementCountAPIView(View):

    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            shopping_cart_id = json_data.get('id')
            shopping_cart = ShoppingCart.objects.get(pk=shopping_cart_id)
            if shopping_cart.count > 0:
                shopping_cart.count -= 1
                shopping_cart.save()
        except Exception as e:
            return JsonResponse({'success': False, 'error': e})
        return JsonResponse({'success': True})


class ChangeCountAPIView(View):

    def post(self, request):
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            shopping_cart_id = json_data.get('id')
            product_count = json_data.get('product_count')

            shopping_cart = ShoppingCart.objects.get(pk=shopping_cart_id)
            if product_count is not None:
                shopping_cart.count = product_count
                shopping_cart.save()
        except Exception as e:
            return JsonResponse({'success': False, 'error': e})
        return JsonResponse({'success': True})


def blog(request):
    return render(request, 'blog.html')


def blog_single(request):
    return render(request, 'blog-single.html')


def contact(request):
    return render(request, 'contact.html')


def services(request):
    service_data = Products.objects.all()
    return render(request, 'services.html', {'services': service_data})
