from django.db import models

class EntregaModel(models.Model):
	data = models.CharField("Data", max_length=100)
	cliente = models.CharField("Cliente", max_length=100)
	endereco = models.CharField("Endereço", max_length=200)
	valor = models.CharField("Valor", max_length=100)
	pendente = models.BooleanField("Pendente", default=True)
	
	def __str__(self):
		return f"{self.cliente} | {self.data} | {self.valor}"
	
	class Meta:
		verbose_name = "Entrega"
		verbose_name_plural = "Entregas"
