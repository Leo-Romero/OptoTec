# Generated by Django 2.2 on 2020-11-23 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0022_pedido_vendedor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='turno',
            options={'ordering': ['-fecha', 'hora'], 'verbose_name': 'Turno', 'verbose_name_plural': 'Turnos'},
        ),
    ]
