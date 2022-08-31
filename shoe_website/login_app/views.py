from unicodedata import category
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Create your views here.

def dashboard(request):
    return render(request, "users/home.html")

def shoes(request):
    return render(request, "users/shoes.html")

def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category':category}
    return render(request, "users/collections.html", context)

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products':products, 'category':category}
        return render(request, 'users/products.html', context)
    else:
        messages.warning(request, "No such category found!")
        return redirect('collections')

def cart(request):
    return render(request, "users/cart.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})



