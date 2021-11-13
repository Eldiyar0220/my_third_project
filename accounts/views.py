
from django.contrib.auth import login, authenticate, get_user_model

from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, FormView, TemplateView
from django.contrib.auth import login as auth_login

from accounts import forms
from accounts.forms import UserRegistrationForm, SignForm, ResetForm

User = get_user_model()

class RegisterViews(CreateView):
    model = User
    template_name = 'pages/registration.html'
    form_class = UserRegistrationForm

    success_url = reverse_lazy('success_registration')

class SuccessfulRegistrationView(TemplateView):
    template_name = 'pages/success_registration.html'

class ActivationView(View):
    def get(self, request):
        code = request.GET.get('u')
        if code:
            user = get_object_or_404(User, activation_code=code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return render(request, 'activation.html', {})
        else:
            return render(request, 'pages/sign.html', status=404)

class art(View):
    def get(self, request):
        User.is_active = False
        User.save()
        return render(request, 'pages/sign.html')

class SignView(LoginView):
    template_name = 'pages/sign.html'
    form_class = SignForm
    success_url = reverse_lazy('home')


class ForgotPasswordView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        email = request.GET.get('email')
        print(1)
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            pk = user.id
            token = user.password
            token = token.replace('/', '')
            url = f'{request.get_host()}{reverse("reset", args=[pk, token])}'
            send_mail("Изменение пароля", f'Чтобы изменить пароль, перейдите по ссылке => {url}',
                      'test@mail.ru', [email], fail_silently=False)
            return JsonResponse({'data': True},status=200)
        else:
            return JsonResponse({'data': False})

def reset(request, pk, token):
    user = User.objects.get(id=pk)
    print(1,user)
    token_db = user.password.replace('/','')
    form = ResetForm()
    if token_db == token and request.method == 'GET':
        return render(request, 'pages/reset_password.html', {'form':form})
    if request.method == 'POST':
        form = ResetForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('new_pass')
            user.set_password(password)
            user.save()
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'pages/404.html')

# def sign(request):
#     if request.method == "POST":
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=email, password=password)
#             login(request, user)
#             return redirect('home')
#         return render(request, 'html', {'form':form})

# smart = SignForm()
# print(1, smart)
#
# def sign(request):
#     if request.method == 'POST':
#         form = SignForm(request.POST)
#         print(form)
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=email, password=password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignForm()
#     return render(request, 'pages/sign.html', {'form':form})

# def sign(request):
#     if request.method == 'POST':
#         form = SignForm(data=request.POST)
#         print(form)
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=email, password=password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignForm()
#     return render(request, 'pages/sign.html', {'form': form})





