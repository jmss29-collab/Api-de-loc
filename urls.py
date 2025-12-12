from django.urls import path
from .views import LocalizacaoListCreate, LocalizacaoDetail

urlpatterns = [
    path('localizacoes/', LocalizacaoListCreate.as_view(), name='localizacao-list'),
    path('localizacoes/<int:pk>/', LocalizacaoDetail.as_view(), name='localizacao-detail'),
]
