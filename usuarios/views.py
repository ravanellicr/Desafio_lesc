from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.

def list_usuarios(request):
	usuarios = Usuario.objects.all()
	return render(request, 'usuarios.html',{'usuarios':usuarios})

def create_usuarios(request):
	form = UsuarioForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('list_usuarios')

	return render(request, 'usuarios-form.html',{'form':form})

def update_usuarios(request, id):
	usuario = Usuario.objects.get(id=id)
	form = UsuarioForm(request.POST or None, instance=usuario)

	if form.is_valid():
		form.save()
		return redirect('list_usuarios')

	return render(request, 'usuarios-form.html',{'form':form,'usuario':usuario})

def delete_usuarios(request, id):
    usuario = Usuario.objects.get(id=id)

    if request.method == 'POST':
        usuario.delete()
        return redirect('list_usuarios')

    return render(request, 'user-delete-confirm.html', {'usuario': usuario})