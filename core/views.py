from django.db.models import query
from django.shortcuts import render
from rest_framework import viewsets
from core.models import Authors, Batch, Books, Client, Order
from core.serializers import BatchSerializer, BooksSerializer, AuthorsSerializer, ClientSerializer,OrderSerializer

class AuthorsViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorsSerializer
    queryset = Authors.objects.all()

class BatchViewSet(viewsets.ModelViewSet):
    serializer_class = BatchSerializer
    queryset = Batch.objects.all()

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

