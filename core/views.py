from django.db.models import query
from django.shortcuts import render
from rest_framework import viewsets
from core.models import Authors, Batch, Books, Client, Order, Usuario
from core.serializers import BatchSerializer, BooksSerializer, AuthorsSerializer, ClientSerializer,OrderSerializer, UsuarioSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class AuthorsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,) 
    serializer_class = AuthorsSerializer
    queryset = Authors.objects.all()

class BatchViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = BatchSerializer
    queryset = Batch.objects.all()

class BooksViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,) 
    serializer_class = BooksSerializer
    queryset = Books.objects.all()

class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()


#DRF nao tem URL pronta de logout
class Logout(APIView):
    def get(self, request):

        request.user.auth_token.delete()
        return Response(' User Logged Out Successfully')
