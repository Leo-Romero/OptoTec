# Generated by Django 2.2 on 2020-11-15 00:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appweb', '0015_auto_20201114_1940'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedido',
            options={'ordering': ['fecha'], 'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='pedido',
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='producto',
        ),
        migrations.AddField(
            model_name='paciente',
            name='medico',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha',
            field=models.DateField(default=datetime.date.today, help_text='Fecha: (DD/MM/AAAA)', verbose_name='Fecha'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='paciente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appweb.Paciente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='tipo_pago',
            field=models.CharField(choices=[('TARJ CREDITO', 'TARJ CREDITO'), ('TARJ DEBITO', 'TARJ DEBITO'), ('BILL. VIRTUAL', 'BILL. VIRTUAL'), ('EFECTIVO', 'EFECTIVO')], default='EFECTIVO', max_length=13, verbose_name='Tipo de pago'),
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appweb.Proveedor'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='producto',
        ),
        migrations.AddField(
            model_name='pedido',
            name='producto',
            field=models.ManyToManyField(to='appweb.Producto'),
        ),
    ]
