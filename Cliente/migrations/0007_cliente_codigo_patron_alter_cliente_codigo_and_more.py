# Generated by Django 4.2.6 on 2023-11-07 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0006_alter_cliente_codigo_alter_cliente_dibujo_patron'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='codigo_patron',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Contrasena/Pin'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='codigo',
            field=models.CharField(blank=True, default='MU1KnsffdV', max_length=10, null=True, verbose_name='codigo de seguimiento'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='dibujo_patron',
            field=models.IntegerField(blank=True, default=0, verbose_name='Patron'),
        ),
    ]