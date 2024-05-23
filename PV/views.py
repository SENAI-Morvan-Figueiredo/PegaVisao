from django.shortcuts import render, get_object_or_404
from PV.models import Atendimento

def index(request):
    atendimento = Atendimento.objects.filter(disponivel=True)
    return render(request, 'clinica/index.html', {"cards": atendimento})

def sobre(request):
    return render(request, 'clinica/sobre.html')

def consulta(request):
    return render(request, 'clinica/consulta.html')

def atendimento(request, atendimento_id):
    atendimento = get_object_or_404(Atendimento, pk=atendimento_id)
    return render(request, 'clinica/atendimento.html', {"atendimento": atendimento})