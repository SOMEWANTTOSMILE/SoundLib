# Generated by Django 5.0.6 on 2024-07-03 12:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='music.category'),
        ),
    ]