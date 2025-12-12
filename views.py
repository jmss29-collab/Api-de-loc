from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Localizacao
from .serializers import LocalizacaoSerializer

class LocalizacaoListCreate(generics.ListCreateAPIView):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer

class LocalizacaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer
