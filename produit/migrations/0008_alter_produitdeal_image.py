# Generated by Django 5.0.3 on 2024-03-23 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0007_alter_grilles_images_alter_topproducts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produitdeal',
            name='image',
            field=models.ImageField(upload_to='media/produitimages/'),
        ),
    ]
