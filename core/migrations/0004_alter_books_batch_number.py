# Generated by Django 4.0 on 2022-01-05 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_authors_books_written_alter_order_purchases'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='batch_number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.batch'),
        ),
    ]