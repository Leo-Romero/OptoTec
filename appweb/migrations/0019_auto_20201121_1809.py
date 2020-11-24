# Generated by Django 2.2 on 2020-11-21 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0018_turno_concurrio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='producto',
        ),
        migrations.AddField(
            model_name='pedido',
            name='producto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appweb.Producto'),
            preserve_default=False,
        ),
    ]