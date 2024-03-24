# Generated by Django 5.0.3 on 2024-03-24 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0014_produitdeal_detail_topproducts_detail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produitdeal',
            name='image_detail_1',
            field=models.ImageField(null=True, upload_to='media/produitimages/'),
        ),
        migrations.AddField(
            model_name='produitdeal',
            name='image_detail_2',
            field=models.ImageField(null=True, upload_to='media/produitimages/'),
        ),
        migrations.AddField(
            model_name='topproducts',
            name='image_detail_1',
            field=models.ImageField(null=True, upload_to='media/topimages/'),
        ),
        migrations.AddField(
            model_name='topproducts',
            name='image_detail_2',
            field=models.ImageField(null=True, upload_to='media/topimages/'),
        ),
        migrations.AlterField(
            model_name='produitdeal',
            name='image',
            field=models.ImageField(null=True, upload_to='media/produitimages/'),
        ),
        migrations.AlterField(
            model_name='topproducts',
            name='image',
            field=models.ImageField(null=True, upload_to='media/topimages/'),
        ),
    ]
