from django.shortcuts import render, redirect
from .models import Producto, Categoria
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

# Create your views here.
def category(request, cate):
    cate = cate.replace("-", " ")
    try:
        categoria = Categoria.objects.get(name=cate)
        productos = Producto.objects.filter(categoria=categoria)
        return render(request, 'category.html', {'productos':productos, 'categoria':categoria})
    except:
        messages.success(request, ("Esa categoria no existe"))
        return redirect('web:home')
def index(request):
    pro = Producto.objects.all()[:6]
    return render(request, 'index.html', {"pro":pro})

def productlisting(request):
    productos = Producto.objects.all()
    return render(request, 'productlisting.html', {'productos':productos})

def profile(request):
    return render(request, 'customerprofile.html', {})

def carrito(request):
    return render(request, 'shoppingcart.html', {})

def configuracion(request):
    return render(request, 'accountsetting.html', {})

def seller(request):
    return render(request, 'sellerprofile.html', {})

def product(request, pk):
    products = Producto.objects.get(id=pk)
    return render(request, 'productdetail.html', {'products':products})

def orders(request):
    return render(request, 'orders.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Has iniciado sesión en tu cuenta"))
            return redirect('web:home')
        else:
            messages.success(request, ("Hubo un error, por favor intenta nuevamente"))
            return redirect('web:login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Has cerrado sesión satisfactoriamente"))
    return redirect('web:home')

def register_user(request):
    form = SignUpForm
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Te has registrado satisfactoriamente"))
            return redirect('web:home')
        else:
            messages.success(request, ("Hubo un error, por favor intenta nuevamente"))
            return redirect('web:register')
    return render(request, 'registration.html', {'form': form})