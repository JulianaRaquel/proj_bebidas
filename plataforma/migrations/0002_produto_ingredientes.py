# Generated by Django 4.1 on 2022-09-20 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='ingredientes',
            field=models.TextField(default='blank'),
        ),
    ]
