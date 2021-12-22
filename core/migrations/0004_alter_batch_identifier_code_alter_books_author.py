# Generated by Django 4.0 on 2021-12-22 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_authors_books_written'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='identifier_code',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.ManyToManyField(to='core.Authors'),
        ),
    ]
