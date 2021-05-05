from django.shortcuts import render, redirect
from .models import Atividade
from .forms import AtividadeForm

# Create your views here.

def list_atividades(request):
	atividades = Atividade.objects.all()
	return render(request, 'atividades.html',{'atividades':atividades})

def create_atividades(request):
	form = AtividadeForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('list_atividades')

	return render(request, 'atividades-form.html',{'form':form})

def update_atividades(request, id):
	atividade = Atividade.objects.get(id=id)
	form = AtividadeForm(request.POST or None, instance=atividade)

	if form.is_valid():
		form.save()
		return redirect('list_atividades')

	return render(request, 'atividades-form.html',{'form':form,'atividade':atividade})

def delete_atividades(request, id):
    atividade = Atividade.objects.get(id=id)

    if request.method == 'POST':
        atividade.delete()
        return redirect('list_atividades')

    return render(request, 'activ-delete-confirm.html', {'atividade': atividade})