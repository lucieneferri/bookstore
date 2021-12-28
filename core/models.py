from django.db import models

class Batch(models.Model):
    identifier_code = models.CharField(max_length=100)
    book_qty = models.IntegerField()
    date_production = models.DateField()

    def __str__(self):
        return self.identifier_code


class Books(models.Model):
    name = models.CharField(max_length=100)
    author = models.ManyToManyField('Authors')
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    batch_number = models.ForeignKey (Batch, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Authors(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    bio = models.TextField()
    books_written = models.ManyToManyField(Books)


    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.IntegerField()
    birth_date = models.DateField

    def __str__(self):
        return self.name


class Order(models.Model):
    order_number = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    order_date = models.DateField()
    value = models.FloatField()
    purchases = models.ManyToManyField(Books)

    def __str__(self):
        return self.order_number + '-' + self.value
