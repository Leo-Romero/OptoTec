# Generated by Django 2.2 on 2020-11-21 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0020_auto_20201121_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appweb.Producto'),
        ),
    ]
