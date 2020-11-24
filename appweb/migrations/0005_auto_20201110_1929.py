# Generated by Django 2.2 on 2020-11-10 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0004_auto_20201110_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='estadciv',
            field=models.CharField(choices=[('SOLTERO/A', 'SOLTERO/A'), ('CASADO/A', 'CASADO/A'), ('DIVORCIADO/A', 'DIVORCIADO/A'), ('VIUDO/A', 'VIUDO/A')], default='SOLTERO/A', max_length=12, verbose_name='Estado civil'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(choices=[('MASCULINO', 'MASCULINO'), ('FEMENINO', 'FEMENINO')], default='MASCULINO', max_length=10, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='puesto',
            field=models.CharField(choices=[('GERENCIA', 'GERENCIA'), ('SECRETARIA', 'SECRETARIA'), ('MEDICO', 'MEDICO'), ('TECNICO', 'TECNICO'), ('VENTAS', 'VENTAS')], default='VENTAS', max_length=10, verbose_name='Puesto'),
        ),
    ]
