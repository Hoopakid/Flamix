from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model, hashers, logout
from django.contrib import messages
from django.views import View

User = get_user_model()


class LoginView(View):
    template_name = 'login.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('/accounts/login')


class RegisterView(View):
    template_name = 'register.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The username already exists')
                return redirect('/accounts/register')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'The email already exists')
                return redirect('/accounts/register')
            else:
                user = User.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                    password=hashers.make_password(password2)
                )
                user.save()
                return redirect('/accounts/login')
        else:
            messages.error(request, "The passwords are not same!!!")
            return redirect('/accounts/register')


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/accounts/login')
