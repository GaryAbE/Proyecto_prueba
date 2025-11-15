from django.contrib import admin
from django.urls import path
from appVentas.views import home
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='login'
    ), name='logout'),
    path('', home, name="home"),
    path('menu/', views.menu , name='menu'),
    path("clientes/", views.lista_clientes, name='lista_clientes'),
    path("nuevo_cliente/", views.crear_cliente, name="crear_cliente"),
    path("eliminar_cliente/<int:id>/", views.eliminar_cliente, name="eliminar_cliente"),
    path("actualizar_cliente/<int:id>/", views.actualizar_cliente, name='actualizar_cliente'),
    
    # TIENDAS
    path("tiendas/", views.listar_tiendas, name='listar_tiendas'),
    path('tiendas/crear/', views.crear_tienda, name='crear_tienda'),
    path('tiendas/editar/<int:id>/', views.editar_tienda, name='editar_tienda'),
    path('tiendas/eliminar/<int:id>/', views.eliminar_tienda, name='eliminar_tienda'),

    # COMPRAS
    path('compras/', views.listar_compras, name='listar_compras'),
    path('compras/crear/', views.crear_compra, name='crear_compra'),
    path('compras/editar/<int:id>/', views.editar_compra, name='editar_compra'),
    path('compras/eliminar/<int:id>/', views.eliminar_compra, name='eliminar_compra'),
]