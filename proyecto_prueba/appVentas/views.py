from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Tienda, Compra
from .forms import ClienteForm, TiendaForm, CompraForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def lista_clientes(request):
    clientes = Cliente.objects.all()  #select * from clientes
    return render(request, 'listar_clientes.html', {'clientes': clientes})

@login_required
def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            Cliente.objects.create(
               nombre = form.cleaned_data['nombre'],
               email = form.cleaned_data['correo'] 
            )
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
        return render(request, 'nuevo_cliente.html',{'form': form})

@login_required
def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente = id)
    cliente.delete()
    return redirect('lista_clientes')

@login_required
def actualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente = id)
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente.nombre = form.cleaned_data['nombre']
            cliente.email = form.cleaned_data['correo']
            cliente.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(initial={
            'nombre': cliente.nombre,
            'correo': cliente.email,
        })
        return render(request, 'actualizar_cliente.html', {'form':form})
    
def listar_tiendas(request):
    tiendas = Tienda.objects.all()
    return render(request, 'tiendas/listar.html', {'tiendas': tiendas})

@login_required
def crear_tienda(request):
    if request.method == "POST":
        form = TiendaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            direccion = form.cleaned_data['direccion']
            # Crear la tienda manualmente
            Tienda.objects.create(nombre=nombre, direccion=direccion)
            return redirect('listar_tiendas')
    else:
        form = TiendaForm()


    return render(request, 'tiendas/crear.html', {'form': form})

@login_required

def editar_tienda(request, id):
    # Obtener la tienda que se va a editar
    tienda = get_object_or_404(Tienda, id_tienda=id)

    if request.method == 'POST':
        form = TiendaForm(request.POST)
        if form.is_valid():
            # Actualizar los campos manualmente
            tienda.nombre = form.cleaned_data['nombre']
            tienda.direccion = form.cleaned_data['direccion']
            tienda.save()
            return redirect('listar_tiendas')
    else:
        # Inicializar el formulario con los datos actuales de la tienda
        form = TiendaForm(initial={
            'nombre': tienda.nombre,
            'direccion': tienda.direccion,
        })

    return render(request, 'tiendas/editar.html', {'form': form})





@login_required
def eliminar_tienda(request, id):
    tienda = Tienda.objects.get(id_tienda=id)

    if request.method == 'POST':
        tienda.delete()
        return redirect('listar_tiendas')

    return render(request, 'tiendas/eliminar.html', {'tienda': tienda})

def listar_compras(request):
    compras = Compra.objects.all()
    return render(request, 'compras/listar.html', {'compras': compras})

@login_required
def crear_compra(request):
    if request.method == "POST":
        form = CompraForm(request.POST)
        if form.is_valid():
            fecha = form.cleaned_data['fecha']
            monto = form.cleaned_data['monto']
            # Crear la compra manualmente
            Compra.objects.create(fecha=fecha, monto=monto)
            return redirect('listar_compras')
    else:
        form = CompraForm()

    return render(request, 'compras/crear.html', {'form': form})

@login_required
def editar_compra(request, id):
    # Obtener la compra que se va a editar
    compra = get_object_or_404(Compra, id_compra=id)

    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            # Actualizar los campos manualmente
            compra.fecha = form.cleaned_data['fecha']
            compra.monto = form.cleaned_data['monto']
            compra.save()
            return redirect('listar_compras')
    else:
        # Inicializar el formulario con los datos actuales de la compra
        form = CompraForm(initial={
            'fecha': compra.fecha,
            'monto': compra.monto,
        })

    return render(request, 'compras/editar.html', {'form': form})

@login_required
def eliminar_compra(request, id):
    compra = Compra.objects.get(id_compra=id)

    if request.method == 'POST':
        compra.delete()
        return redirect('listar_compras')

    return render(request, 'compras/eliminar.html', {'compra': compra})

def home(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'MenuPrincipal.html'
)



