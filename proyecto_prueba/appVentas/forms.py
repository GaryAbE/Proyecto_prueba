from django import forms


class ClienteForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    correo = forms.EmailField(label="Correo", required=True)

class CompraForm(forms.Form):
    fecha = forms.DateField(label="Fecha de Compra", required=True, widget=forms.SelectDateWidget)
    monto = forms.DecimalField(label="Monto", required=True, max_digits=10, decimal_places=2)

class TiendaForm(forms.Form):
    nombre = forms.CharField(label="Nombre de la Tienda", required=True)
    direccion = forms.CharField(label="Dirección", required=True, max_length=150)