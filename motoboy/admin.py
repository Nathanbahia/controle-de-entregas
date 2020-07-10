from django.contrib import admin

from .models import EntregaModel

@admin.register(EntregaModel)
class EntregaModelAdmin(admin.ModelAdmin):
	list_display = ("data", "cliente", "endereco", "valor", "pendente")
