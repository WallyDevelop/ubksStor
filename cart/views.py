from django.shortcuts import render, get_object_or_404
from .cart import Cart
from web.models import Producto
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    return render(request, 'shoppingcart.html', {})

def cart_add(request):
    '''cart = Cart(request)
    if request.POST.get('action') == 'post':
        products_id = int(request.POST.get('products_id'))
        product = get_object_or_404(Producto, id=products_id)
        cart.add(product=product)
        response = JsonResponse({'Nombre Producto': product.nombre})
        return response'''

def cart_delete(request):
    pass

def cart_update(request):
    pass