# Generated by Django 2.2 on 2020-11-10 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0002_perfil_interno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cobertura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre', max_length=50, verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, help_text='Descripción', max_length=100, null=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Cobertura',
                'verbose_name_plural': 'Coberturas',
                'ordering': ['nombre'],
            },
        ),
        migrations.AlterField(
            model_name='perfil',
            name='interno',
            field=models.CharField(blank=True, help_text='Número de interno (i.e 1234)', max_length=4, null=True, verbose_name='Interno Tel.'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='telefono',
            field=models.CharField(blank=True, help_text='Teléfono particular (i.e 2923-4123456)', max_length=12, null=True, verbose_name='Teléfono'),
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(help_text='Número de DNI', max_length=8, verbose_name='DNI')),
                ('apellido', models.CharField(blank=True, help_text='Apellido', max_length=50, null=True, verbose_name='Ciudad')),
                ('nombres', models.CharField(blank=True, help_text='Nombres', max_length=250, null=True, verbose_name='Ciudad')),
                ('num_cobertura', models.CharField(help_text='Número de afiliado', max_length=8, verbose_name='#')),
                ('f_nac', models.DateField(blank=True, help_text='Fecha de nacimiento: (DD/MM/AAAA)', null=True, verbose_name='Fecha de nacimiento')),
                ('sexo', models.CharField(choices=[('MASCULINO', 'MASCULINO'), ('FEMENINO', 'FEMENINO')], default='MASCULINO', max_length=10, verbose_name='Sexo')),
                ('direccion', models.CharField(blank=True, help_text='(i.e Chiclana 555)', max_length=60, null=True, verbose_name='Dirección')),
                ('ciudad', models.CharField(blank=True, help_text='(i.e Bahia Blanca)', max_length=50, null=True, verbose_name='Ciudad')),
                ('telefono', models.CharField(blank=True, help_text='(i.e 2923-4123456)', max_length=12, null=True, verbose_name='Teléfono')),
                ('cobertura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appweb.Cobertura')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'ordering': ['dni'],
            },
        ),
    ]
