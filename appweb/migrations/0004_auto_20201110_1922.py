# Generated by Django 2.2 on 2020-11-10 22:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0003_auto_20201110_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='correo',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='estadciv',
            field=models.CharField(choices=[('SOLTERO/A', 'SOLTERO/A'), ('CASADO/A', 'CASADO/A'), ('DIVORCIADO/A', 'DIVORCIADO/A'), ('VIUDO/A', 'VIUDO/A')], default='SOLTERO/A', max_length=1, verbose_name='Estado civil'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='ocupacion',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Ocupación'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='apellido',
            field=models.CharField(blank=True, help_text='Apellido', max_length=50, null=True, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='ciudad',
            field=models.CharField(blank=True, help_text='(e.g. Bahia Blanca)', max_length=50, null=True, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='direccion',
            field=models.CharField(blank=True, help_text='(e.g. Chiclana 555)', max_length=60, null=True, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nombres',
            field=models.CharField(blank=True, help_text='Nombres', max_length=250, null=True, verbose_name='Nombres'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='num_cobertura',
            field=models.CharField(help_text='Número de afiliado', max_length=25, verbose_name='Afiliado'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(choices=[('MASCULINO', 'MASCULINO'), ('FEMENINO', 'FEMENINO')], default='MASCULINO', max_length=1, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefono',
            field=models.CharField(blank=True, help_text='(e.g. 2923-4123456)', max_length=12, null=True, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='interno',
            field=models.CharField(blank=True, help_text='Número de interno (e.g. 1234)', max_length=4, null=True, verbose_name='Interno Tel.'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='puesto',
            field=models.CharField(choices=[('GERENCIA', 'GERENCIA'), ('SECRETARIA', 'SECRETARIA'), ('MEDICO', 'MEDICO'), ('TECNICO', 'TECNICO'), ('VENTAS', 'VENTAS')], default='VENTAS', max_length=2, verbose_name='Puesto'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='telefono',
            field=models.CharField(blank=True, help_text='Teléfono particular (e.g. 2923-4123456)', max_length=12, null=True, verbose_name='Teléfono'),
        ),
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, default=datetime.date.today, help_text='Fecha: (DD/MM/AAAA)', null=True, verbose_name='Fecha')),
                ('motivo', models.TextField(blank=True, null=True, verbose_name='Motivo')),
                ('enf_actual', models.TextField(blank=True, null=True, verbose_name='Enf. Actual')),
                ('antecedentes', models.TextField(blank=True, null=True, verbose_name='Antecedentes')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appweb.Paciente')),
            ],
            options={
                'verbose_name': 'Historia',
                'verbose_name_plural': 'Historias',
                'ordering': ['fecha'],
            },
        ),
    ]
