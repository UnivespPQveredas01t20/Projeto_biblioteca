# Generated by Django 2.1.15 on 2021-11-18 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipousuario',
            name='nik_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Apelido'),
        ),
    ]
