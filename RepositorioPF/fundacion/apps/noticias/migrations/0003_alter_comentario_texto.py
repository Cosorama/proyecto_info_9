# Generated by Django 3.2 on 2022-08-26 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='texto',
            field=models.TextField(blank=True, null=True),
        ),
    ]