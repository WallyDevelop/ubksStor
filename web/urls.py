from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    path('ordenes/', views.orders, name='ordenes'),
    path('producto/<int:pk>', views.product, name='producto'),
    path('vendedor/', views.seller, name='vendedor'),
    path('config/', views.configuracion, name='config'),
    #path('carrito/', views.carrito, name='carrito'),
    path('', views.index, name='home'),
    path('perfil/', views.profile, name='perfil'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('productlisting/', views.productlisting, name='productolis'),
    path('register/', views.register_user, name='register'),
    path('category/<str:cate>', views.category, name='category'),
]