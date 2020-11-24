# Generated by Django 2.2 on 2020-11-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0030_auto_20201123_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='cerca',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='derecho',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='izquierdo',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='lejos',
        ),
        migrations.AddField(
            model_name='producto',
            name='distancia',
            field=models.CharField(blank=True, choices=[('LEJOS', 'LEJOS'), ('CERCA', 'CERCA')], default='LEJOS', max_length=5, null=True, verbose_name='Distancia'),
        ),
        migrations.AddField(
            model_name='producto',
            name='lado',
            field=models.CharField(blank=True, choices=[('IZQUIERDO', 'IZQUIERDO'), ('DERECHO', 'DERECHO')], default='IZQUIERDO', max_length=9, null=True, verbose_name='Ojo'),
        ),
        migrations.AddField(
            model_name='producto',
            name='lente',
            field=models.BooleanField(default=False, verbose_name='Lente ?'),
        ),
    ]