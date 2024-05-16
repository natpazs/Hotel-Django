# Generated by Django 5.0.5 on 2024-05-16 17:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_quarto_foto_quarto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('idade', models.IntegerField()),
                ('endereco', models.CharField(max_length=60)),
                ('quarto', models.CharField(choices=[('SOLTEIRO', 'Solteiro'), ('CASAL', 'Casal'), ('CONFORTO', 'Conforto'), ('LUXO', 'Luxo')], max_length=15)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
