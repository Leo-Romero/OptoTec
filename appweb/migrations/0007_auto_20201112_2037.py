# Generated by Django 2.2 on 2020-11-12 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0006_auto_20201111_1752'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paciente',
            options={'ordering': ['dni'], 'permissions': (('puede_ver', 'Puede acceder a Pacientes'),), 'verbose_name': 'Paciente', 'verbose_name_plural': 'Pacientes'},
        ),
    ]
