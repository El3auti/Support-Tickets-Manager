# Generated by Django 4.2.6 on 2023-11-20 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0015_alter_servicio_tecnico'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='mensaje',
            field=models.CharField(max_length=500, null=True, verbose_name='Mensaje que se enviara'),
        ),
    ]
