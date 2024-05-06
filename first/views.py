import random
from django.shortcuts import redirect, render
from .models import Category,T_shirts, Buy,Avertising
from .forms import *
import numpy as np
# Create your views here.

def home(request):
    ctg = Category.objects.all()
    advertising = Avertising.objects.all()
    t_shirt = T_shirts.objects.all()
    random_t_shirts = random.choice(advertising)
    ctx = {
        'ctg': ctg,
        't_shirt': t_shirt,
        'random_shirt': random_t_shirts,
    }

    return render(request, 'blog/index.html', ctx)

def contact(request):
    ctg = Category.objects.all()
    form = ContactForms()
    if request.POST:
        forms = ContactForms(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    ctx = {'ctg': ctg}
    return render(request, 'blog/contact.html', ctx)

def products(request, slug=None):
    ctg = Category.objects.all()
    category = Category.objects.get(slug=slug)
    t_shirt = T_shirts.objects.all().filter(type_id=category.id)
    ctx = {
        'ctg': ctg,
        't_shirt': t_shirt,
        'category': category,
    }
    return render(request, 'blog/products.html', ctx)

def register(request):
    ctg = Category.objects.all()
    form = RegisterForm()
    if request.POST:
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    ctx = {'ctg':ctg}
    return render(request, 'blog/register.html', ctx)



def single(request, pk=None):
    ctg = Category.objects.all()
    t_shirt = T_shirts.objects.all()
    random_t_shirts = np.random.choice(t_shirt, size=3, replace=False)
    products_pk = T_shirts.objects.get(pk = pk)
    form = ChoiseForm
    if request.POST:
        forms = ChoiseForm(request.POST or None,
                           request.FILES or None)
        if forms.is_valid():
            root = forms.save()
            root = Buy.objects.get(pk=root.id)
            root.products = products_pk
            root.save()
            return redirect('home')
        else:
            print(forms.errors)
    ctx = {
        'ctg': ctg,
        'random_t_shirts': random_t_shirts,
        't_shirt': t_shirt,
        'products_pk': products_pk,
        'form': form,
    }
    return render(request, 'blog/single.html', ctx)