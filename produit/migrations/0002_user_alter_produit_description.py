# Generated by Django 5.0.3 on 2024-03-20 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('date_creation', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='produit',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
