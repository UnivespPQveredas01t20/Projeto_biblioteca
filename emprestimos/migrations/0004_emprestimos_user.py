# Generated by Django 2.1.15 on 2021-11-18 02:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('emprestimos', '0003_emprestimos_data_emprestimo'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimos',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
