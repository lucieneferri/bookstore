from rest_framework import serializers
from .models import Batch, Books, Authors, Client, Order

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = [
            'id',
            'identifier_code',
            'book_qty',
            'date_production'
        ]

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = [
            'id',
            'name',
            'author',
            'release_date',
            'genre',
            'batch_number'
        ]

class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = [
            'id',
            'name',
            'country',
            'genre',
            'bio'
        ]

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Client
        fields = [
            'id',
            'name',
            'cpf',
            'birth_date'
        ]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',
            'order_number',
            'client',
            'order_date',
            'value',
            'purchases'
        ]