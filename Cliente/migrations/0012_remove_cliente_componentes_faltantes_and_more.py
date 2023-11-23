# Generated by Django 4.2.6 on 2023-11-14 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0011_remove_cliente_direccion_remove_cliente_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='componentes_faltantes',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='observaciones',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='codigo',
            field=models.CharField(blank=True, default=models.AutoField(primary_key=True, unique=True), max_length=10, null=True, verbose_name='codigo de seguimiento'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fisuras',
            field=models.BooleanField(default=False, verbose_name='Fisuras/Quebraduras'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='golpes_graves',
            field=models.BooleanField(default=False, verbose_name='Golpes Graves'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='golpes_leves',
            field=models.BooleanField(default=False, verbose_name='Golpes leves'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='manchas',
            field=models.BooleanField(default=False, verbose_name='Manchas'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='marcas',
            field=models.BooleanField(default=False, verbose_name='Marcas/Rayones'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='pintura',
            field=models.BooleanField(default=False, verbose_name='Pintura dañada'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipo_reparacion',
            field=models.CharField(choices=[('Reparacion por garantia', 'Reparacion por garantia'), ('reparacion por cuenta del cliente', 'reparacion por cuenta del cliente')], default='reparacion por cuenta del cliente', max_length=200, verbose_name='tipo de reparacion'),
        ),
    ]
