# Generated by Django 4.0.1 on 2022-01-19 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_books_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
