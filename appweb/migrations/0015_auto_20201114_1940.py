# Generated by Django 2.2 on 2020-11-14 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0014_auto_20201114_1729'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paciente',
            options={'ordering': ['dni'], 'verbose_name': 'Paciente', 'verbose_name_plural': 'Pacientes'},
        ),
        migrations.RemoveField(
            model_name='producto',
            name='proveedor',
        ),
        migrations.AddField(
            model_name='proveedor',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appweb.Producto'),
        ),
    ]
