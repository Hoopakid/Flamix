from django.shortcuts import render, redirect
from .models import Service, ShoppingCart, Image, Products
from django.views import View
from django.db.models import Q
from django.contrib import messages


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
        service_id = request.POST.get('serivce_id')
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


def blog(request):
    return render(request, 'blog.html')


def blog_single(request):
    return render(request, 'blog-single.html')


def contact(request):
    return render(request, 'contact.html')


def services(request):
    service_data = Service.objects.all()
    return render(request, 'services.html', {'services': service_data})
