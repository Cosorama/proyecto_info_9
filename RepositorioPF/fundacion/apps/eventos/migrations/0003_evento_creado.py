# Generated by Django 3.2 on 2022-08-30 00:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_alter_evento_lugar'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='creado',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
