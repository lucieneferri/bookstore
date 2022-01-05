from rest_framework import serializers
from .models import Batch, Books, Authors, Client, Order, Usuario

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

class UsuarioSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Senha"
    )

    password_confirm = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Confirme a senha"
    )

    is_staff = serializers.BooleanField(
        label="Membro da Equipe",
        help_text="Indica que usuário consegue acessar o site de administração."
    )

    is_superuser = serializers.BooleanField(
        label="SuperUsuário",
        help_text="Indica que este usuário tem todas as permissões sem atribuí-las explicitamente."
    )
    
    
    class Meta:
        model = Usuario
        fields = [
            'id',
            'username',
            'password',
            'password_confirm',
            'email',
            'is_staff',
            'is_superuser'
        ]
    def save(self):

        conta = Usuario(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            is_staff = self.validated_data['is_staff'],
            is_superuser = self.validated_data['is_superuser']
        )

        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']

        if password != password_confirm:
            raise serializers.ValidationError({'password':'As senhas não são iguais.'})
        else:
            conta.set_password(password)
            conta.save()
            return conta
    