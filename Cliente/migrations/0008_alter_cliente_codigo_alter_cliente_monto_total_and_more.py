# Generated by Django 4.2.6 on 2023-11-07 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0007_cliente_codigo_patron_alter_cliente_codigo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='codigo',
            field=models.CharField(blank=True, default='hhR1tNyIKS', max_length=10, null=True, verbose_name='codigo de seguimiento'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='monto_total',
            field=models.IntegerField(blank=True, default='$', null=True, verbose_name='Monto total (Aprox)'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='parte_pago',
            field=models.IntegerField(blank=True, default='$', null=True, verbose_name='Pago por adelantado'),
        ),
    ]
