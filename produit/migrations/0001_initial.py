# Generated by Django 5.0.3 on 2024-03-22 13:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grilles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_grille', models.CharField(max_length=200)),
                ('images', models.ImageField(default='default_image.jpg', upload_to='static/images/')),
                ('date_ajout', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-date_ajout'],
            },
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_pronduit', models.CharField(max_length=200)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=100)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='static/images/')),
                ('off', models.DecimalField(decimal_places=2, max_digits=100)),
                ('like', models.BooleanField(default=False)),
                ('date_ajout', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-date_ajout'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(default='email@email.com', max_length=254, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('date_creation', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
