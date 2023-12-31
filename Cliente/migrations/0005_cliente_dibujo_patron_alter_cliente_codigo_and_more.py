# Generated by Django 4.2.6 on 2023-11-05 20:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0004_alter_cliente_codigo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='dibujo_patron',
            field=models.IntegerField(blank=True, default=0, verbose_name='Patron del usuario'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='codigo',
            field=models.CharField(blank=True, default='jwbuLT0PKX', max_length=10, null=True, verbose_name='codigo de seguimiento'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='estado',
            field=models.CharField(blank=True, choices=[('En Arreglo', 'En Arreglo'), ('Listo para retirar', 'Listo para retirar'), ('Aceptado', 'Aceptado'), ('No se puede arreglar', 'No se puede arreglar')], max_length=20, null=True, verbose_name='Estado del pedido'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_deja_prod',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha entrada'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_terminacion_prod',
            field=models.DateTimeField(verbose_name='Fecha Salida'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre_apellido',
            field=models.CharField(default='', max_length=126, null=True, verbose_name='Nombre y Apellido'),
        ),
    ]
