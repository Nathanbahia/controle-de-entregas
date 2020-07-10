from django import forms
from .models import EntregaModel

class EntregaModelForm(forms.ModelForm):
	class Meta:
		model = EntregaModel
		fields = ["data", "cliente", "endereco", "valor"]
		