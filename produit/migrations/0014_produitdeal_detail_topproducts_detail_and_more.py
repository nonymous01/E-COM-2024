# Generated by Django 5.0.3 on 2024-03-24 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0013_rename_name_pronduit_topproducts_name_produit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produitdeal',
            name='detail',
            field=models.TextField(max_length=100000000, null=True),
        ),
        migrations.AddField(
            model_name='topproducts',
            name='detail',
            field=models.TextField(max_length=100000000, null=True),
        ),
        migrations.AlterField(
            model_name='produitdeal',
            name='name_pronduit',
            field=models.CharField(max_length=200),
        ),
    ]