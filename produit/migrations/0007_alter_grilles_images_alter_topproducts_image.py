# Generated by Django 5.0.3 on 2024-03-23 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0006_alter_topproducts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grilles',
            name='images',
            field=models.ImageField(default='default_image.jpg', upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='topproducts',
            name='image',
            field=models.ImageField(upload_to='media/topimages/'),
        ),
    ]
