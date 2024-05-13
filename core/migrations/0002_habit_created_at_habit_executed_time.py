# Generated by Django 4.2 on 2024-05-13 18:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='время создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='habit',
            name='executed_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='время выполнения'),
        ),
    ]