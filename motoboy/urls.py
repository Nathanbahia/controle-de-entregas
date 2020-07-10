from django.urls import path
from .views import IndexView, recebimentos, confirma_recebimento

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('recebimentos.html/<int:pk>/', recebimentos, name="recebimentos"),
    path('baixa.html/<int:pk>/', confirma_recebimento, name="baixa"),
    ]