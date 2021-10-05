from django.http import HttpResponse
from django.shortcuts import render
from accounts.forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.set_password(form.cleaned_data['password'])
            new_form.save()
            return HttpResponse('Вы успешно заргистрировались')
        return render(request, 'pages/registration.html', {'form':form})
    else:
        form = UserRegistrationForm()
        return render(request, 'pages/registration.html', {'form':form})