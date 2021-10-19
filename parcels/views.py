from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from parcels.models import Parcels
from parcels.forms import OrderCreateForm, OrderUpdateForm


def parcels(request):
    parcels_form = OrderCreateForm()
    form_object = Parcels.objects.filter(order=request.user)
    paginator = Paginator(form_object, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pages/s.html',{"parcels_form":parcels_form,"page_obj":page_obj})

# class ParcelsCreateView(CreateView):
#     model  = Parcels
#     fields = ['recipient']
#     template_name = 'pages/parcels.html'
#     success_url = ('home')

def ChangeProfileView(request):
    if request.method == 'POST':
        edit = OrderUpdateForm(request.POST, request.FILES, instance=request.user)
        print(edit)
        if edit.is_valid():
            edit.save()
            return HttpResponseRedirect(reverse_lazy('profile'))
    else:
        edit = OrderUpdateForm(instance=request.user)
    return render(request, 'pages/s.html', { 'edit': edit })
