# Generated by Django 5.0.3 on 2024-03-24 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0020_alter_produitdeal_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topproducts',
            name='stock',
            field=models.CharField(choices=[('En stock', 'En stock'), ('Disponible', 'Disponible'), ('Indisponible', 'Indisponible')], default='Disponible', max_length=200),
        ),
    ]