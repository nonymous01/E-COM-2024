# Generated by Django 5.0.3 on 2024-03-22 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0002_alter_produit_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='prix',
            field=models.DecimalField(decimal_places=0, max_digits=100),
        ),
    ]
