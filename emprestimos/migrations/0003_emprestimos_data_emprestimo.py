# Generated by Django 2.1.15 on 2021-11-18 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimos', '0002_auto_20211117_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateField(blank=True, help_text='Informar a Data em que o item está sendo emprestado!', null=True),
        ),
    ]
