# Generated by Django 5.0.3 on 2024-03-24 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0016_topproducts_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='produitdeal',
            name='stock',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
