from django.shortcuts import render, redirect
from .models import Corsi
# Create your views here.
from corsi.forms import AlunnoForm


def index(request):
    corsi = Corsi.objects.all()
    return render(request, 'corsi/index.html', {"corsi": corsi})

def corso_singolo(request, corso_id):
    try:
        corso = Corsi.objects.get(pk=corso_id)
        return render(request, 'corsi/corso_singolo.html', {"corso": corso})
    except:
        return redirect("corsiHome")

def registrazioneAlunno(request):
    if request.method == "POST":
        form = AlunnoForm(request.POST, request.FILES)
        if form.is_valid():
            alunno = form.save(commit=False)
            alunno.save()
            return redirect("/")
    else:
        form = AlunnoForm()
    return render(request, 'corsi/registration.html', {"form": form})
