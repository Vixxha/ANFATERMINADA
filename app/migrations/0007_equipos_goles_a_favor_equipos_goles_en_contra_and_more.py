# Generated by Django 5.0.1 on 2024-02-08 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_noticia_options_remove_equipos_cantidad_goles_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipos',
            name='goles_a_favor',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='equipos',
            name='goles_en_contra',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='equipos',
            name='partidos_empatados',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='equipos',
            name='partidos_ganados',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='equipos',
            name='partidos_perdidos',
            field=models.IntegerField(default=0),
        ),
    ]
