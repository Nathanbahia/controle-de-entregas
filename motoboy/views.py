from django.views.generic import FormView, DetailView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import EntregaModel
from .forms import EntregaModelForm

class IndexView(FormView):
	template_name = "index.html"
	form_class = EntregaModelForm
	success_url = reverse_lazy("index")
	
	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context["entregas"] = EntregaModel.objects.filter(pendente=True)
		context["qtde_entregas"] = len(EntregaModel.objects.all())
		context["entregas_recebidas"] = len(EntregaModel.objects.filter(pendente=False))
		context["entregas_pendentes"] = len(EntregaModel.objects.filter(pendente=True))
		return context

	def form_valid(self, form):
		form.save()
		return super(IndexView, self).form_valid(form)
	
	def form_invalid(self, form):
		return super(IndexView, self).form_invalid(form)


def recebimentos(request, pk):
    entrega = EntregaModel.objects.get(id=pk)
    context = {"entrega": entrega}
    return render(request, "recebimentos.html", context)
    
def confirma_recebimento(request, pk):
	baixa = EntregaModel.objects.get(id=pk)
	baixa.pendente = False
	baixa.save()
	return redirect("index")