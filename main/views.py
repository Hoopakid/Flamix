import json

from django.views import View
from django.db.models import Q
from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Products, Image, ShoppingCart, Comment, ComboProducts, ShoppingCartCombo, Order, Message


class HomeTemplateView(View):
    template_name = 'index.html'
    context = {}

    def get(self, request):
        service_data = Products.objects.all()
        comments = Comment.objects.all().order_by('-created_at')[:4]
        services_data = []
        for service in service_data:
            image = Image.objects.filter(service=service).first()
            service.image = image
            services_data.append(service)
        self.context.update({'service_data': services_data})
        self.context.update({'comments': comments})
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


class CommentView(View):
    template_name = 'comment.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        message = request.POST.get('message')
        is_anonymous = request.POST.get('is_anonymous')
        user = None if is_anonymous == 'on' else request.user
        print(message, user, is_anonymous)
        comment = Comment.objects.create(
            message=message,
            user=user,
        )
        comment.save()
        return redirect('/')


class ServicesView(View):
    template_name = 'services.html'
    context = {}

    def get(self, request):
        combo_products = ComboProducts.objects.all()
        self.context.update({'combo_products': combo_products})
        return render(request, self.template_name, self.context)

    def post(self, request):
        combo_product_id = request.POST.get('combo_product_id')
        user = request.user
        combo_product_instance = get_object_or_404(ComboProducts, pk=combo_product_id)
        if not ShoppingCartCombo.objects.filter(Q(user=user) & Q(combo_id=combo_product_instance)).exists():
            shopping_cart_combo = ShoppingCartCombo.objects.create(
                user=user, combo_id=combo_product_instance
            )
            shopping_cart_combo.save()
            messages.info(request, 'Product added successfully !!!')
            return redirect('/services')

        messages.error(request, 'This service already exists in cart')
        return redirect('/services')


class ComboShoppingCartTemplateView(View):
    template_name = 'combo_shopping_cart.html'
    context = {}

    def get(self, request):
        combo_products = ShoppingCartCombo.objects.all()
        self.context.update({'combo_products': combo_products})
        return render(request, self.template_name, self.context)

    def post(self, request):
        combo_id = request.POST.get('shopping_cart_combo_id')
        ShoppingCartCombo.objects.get(pk=combo_id).delete()
        return redirect('/combo')


class AddProductView(View):
    template_name = 'add_product.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        title = request.POST.get('title')
        cost = request.POST.get('cost')
        images = request.FILES.getlist('images')

        service = Products.objects.create(
            title=title,
            cost=cost,
            author=request.user
        )
        service.save()
        for image in images:
            img = Image.objects.create(
                img=image,
                service=service
            )
            img.save()
        return redirect('/add-product')


class OrderTemplateView(View):
    template_name = 'checkout.html'
    context = {}

    def get(self, request):
        service = ShoppingCart.objects.select_related('service').filter(user=request.user)
        self.context.update({'service': service})
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        services = ShoppingCart.objects.select_related('service').filter(user=request.user)
        for service in services:
            order = Order.objects.create(
                user=request.user,
                service=service.service,
                count=service.count,
                status=1
            )
            order.save()
        return redirect(request, self.template_name, self.context)


class ContactTemplateView(View):
    template_name = 'contact.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        name = request.POST.get('name')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        website = request.POST.get('website')
        print(name, email, subject, message, website)
        message = Message.objects.create(
            name=name, email=email, website=website,
            subject=subject, message=message
        )
        message.save()
        return redirect('/contact')


def blog(request):
    return render(request, 'blog.html')


def blog_single(request):
    return render(request, 'blog-single.html')


def quality_printing(request):
    return render(request, 'quality_printing.html')


def ontime_delivery(request):
    return render(request, 'ontime_delivery.html')


def support(request):
    return render(request, '24_7_support.html')


def money_back_guarantee(request):
    return render(request, 'money_back_guarantee.html')
