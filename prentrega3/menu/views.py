from django.shortcuts import render
from menu.models import Compras, Usuario, Distribuidor
from menu.forms import usuarioForm, distribuidorForm, productoForm

def home(request):

    compra = Compras.objects.all()

    return render(request,'menu/index.html',{"compra":compra})


def usuario(request):
    if request.method == "POST":
        user_form = usuarioForm(request.POST)
        if user_form.is_valid():
            data = user_form.cleaned_data
            user = Usuario(nombre=data["name"], correo=data["email"], edad=data["age"])
            user.save()
            return render(request, 'menu/end_user.html') # Render success template
    else:
        user_form = usuarioForm()
    return render(request, 'menu/end_user.html', {'user_form': user_form})


def distribuidor(request):
    if request.method == "POST":
        distri_form = distribuidorForm(request.POST)
        if distri_form.is_valid():
            info = distri_form.cleaned_data
            distributor = Distribuidor(nombre=info["name"], correo = info["email"], compañia = info["company"], distri_codigo = info["distributor_numbre"])
            distributor.save()
            return render(request, 'menu/distributor.html') # Render success template
    else:
        distri_form = distribuidorForm()
    return render(request, 'menu/distributor.html', {'distri_form': distri_form})

def registro(request):
    if request.method == "POST":
        product_form = productoForm(request.POST)
        if product_form.is_valid():
            data = product_form.cleaned_data
            producto= Compras(nombre=data["name"], codigo=data["product_code"], precio=data["price"])
            producto.save()
            return render(request, 'menu/product_registration.html') # Render success template
    else:
        product_form = productoForm()
    return render(request, 'menu/product_registration.html', {'product_form': product_form})

def buscar(request):
    
    if request.method == "POST":

            produc = Compras.objects.filter(codigo =int(request.POST["codigo"]))

            return render(request, 'menu/buscar_producto.html', {"infor":[produc]}) # Render success template
    else:
        product_form = productoForm()
    return render(request, 'menu/buscar_producto.html', {'product_form': product_form})
