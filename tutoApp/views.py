from django.shortcuts import render
from rest_framework import generics

from tutoApp.models import Deposito, Articulo
from tutoApp.serializers import DepositoSerializer, ArticuloSerializer
# Create your views here.

class DepositoList(generics.ListCreateAPIView):
    queryset = Deposito.objects.all()
    serializer_class = DepositoSerializer

class DepositoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deposito.objects.all()
    serializer_class = DepositoSerializer

class ArticuloList(generics.ListCreateAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

class ArticuloDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer





