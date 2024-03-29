# Generated by Django 5.0.3 on 2024-03-22 15:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0004_rename_produit_produitdeal'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_pronduit', models.CharField(max_length=200)),
                ('prix', models.DecimalField(decimal_places=0, max_digits=100)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='static/produitimages/')),
                ('off', models.DecimalField(decimal_places=2, max_digits=100)),
                ('like', models.BooleanField(default=False)),
                ('date_ajout', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-date_ajout'],
            },
        ),
    ]
