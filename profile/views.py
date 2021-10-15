from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse

from django.views.generic import TemplateView, UpdateView
from profile.forms import UserEditForm
User = get_user_model()

class MainProfileView(TemplateView):
    template_name = 'pages/personal-area.html'


# class ChangeProfileView(UpdateView):
#     model = User
#     form_class = UserEditForm
#     template_name = 'pages/change-profile.html'

def ChangeProfileView(request):
    if request.method == 'POST':
        edit = UserEditForm(request.POST, request.FILES, instance=request.user)
        print(edit)
        if edit.is_valid():
            edit.save()
            return HttpResponseRedirect(reverse_lazy('profile'))
    else:
        edit = UserEditForm(instance=request.user)
    return render(request, 'pages/change-profile.html', { 'edit': edit })

