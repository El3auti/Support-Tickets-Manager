# Generated by Django 4.2.6 on 2023-11-07 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cliente', '0009_alter_cliente_codigo_alter_cliente_monto_total_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='codigo',
            field=models.CharField(blank=True, default='vneex2tkr1', max_length=10, null=True, verbose_name='codigo de seguimiento'),
        ),
    ]
