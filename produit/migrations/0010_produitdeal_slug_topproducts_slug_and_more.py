# Generated by Django 5.0.3 on 2024-03-23 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0009_alter_grilles_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='produitdeal',
            name='slug',
            field=models.SlugField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='topproducts',
            name='slug',
            field=models.SlugField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='produitdeal',
            name='name_pronduit',
            field=models.CharField(max_length=2000),
        ),
    ]
