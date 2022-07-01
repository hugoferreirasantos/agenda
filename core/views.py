from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.

# def index(request):
#     return redirect('/agenda/')
def lista_eventos(request):
    evento = Evento.objects.all()
    # usuario = request.user
    # evento = Evento.objects.filter(usuario=usuario)
    dados  = {'eventos':evento}
    return render(request, 'agenda.html', dados)