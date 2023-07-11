from django.contrib import admin
from . models import Corsi, ToDoCategory, Alunno
# Register your models here.

admin.site.register(ToDoCategory)

# Serve per vedere il campo img preview nell'area admin
class CorsiAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']

admin.site.register(Corsi, CorsiAdmin)
admin.site.register(Alunno)