# Generated by Django 5.0.3 on 2024-03-24 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0019_alter_topproducts_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produitdeal',
            name='stock',
            field=models.CharField(choices=[('En stock', 'En stock'), ('Disponible', 'Disponible'), ('Indisponible', 'Indisponible')], default='Disponible', max_length=20),
        ),
    ]
