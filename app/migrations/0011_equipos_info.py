# Generated by Django 5.0.1 on 2024-02-10 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_equipos_diferencia_goles'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipos',
            name='info',
            field=models.TextField(null=True),
        ),
    ]