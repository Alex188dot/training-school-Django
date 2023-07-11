from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe

# Create your models here.


class ToDoCategory(models.Model):
    titolo = models.CharField('Titolo della Categoria',max_length = 200)
    descrizione = models.CharField('Descrizione della Categoria',max_length = 250)

    def __str__(self):
        return self.titolo
    class Meta:
        verbose_name_plural = "Categorie"


class Corsi(models.Model):
    # vado a delianare i campi della tabella
    titolo = models.CharField(max_length=150)
    img = models.ImageField(upload_to='img/corsi', default=None)
    contenuto = models.TextField()
    data_inizio = models.DateField()
    durata_ore = models.DecimalField(decimal_places=0, max_digits=3)
    docente = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    prezzo = models.DecimalField(decimal_places=0, max_digits=10)
    categoria = models.ForeignKey(ToDoCategory, on_delete = models.CASCADE)

    def __str__(self):
        return self.titolo
    # Creo il metodo per visualizzare l'img in admin
    def img_preview(self):
        return mark_safe(f'<img src="{self.img.url}" width="300" height="300"/>')
    class Meta:
        verbose_name_plural = "Corsi"
        


class Alunno(models.Model):
    nome = models.CharField('Nome', max_length=200)
    cognome = models.CharField('Cognome', max_length=200)
    email = models.CharField('Email', max_length=200)
    telefono = models.CharField('Telefono', max_length=200)
    corso = models.ForeignKey(Corsi, on_delete=models.CASCADE,  null=True)
    img = models.ImageField(upload_to='img/utenti')

    def __str__(self):
        return f"{self.nome} {self.cognome}"

    class Meta:
        verbose_name_plural = "Alunni"
