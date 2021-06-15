# Generated by Django 3.2.4 on 2021-06-15 20:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('barbershopapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work_schedule',
            name='datetime',
        ),
        migrations.AddField(
            model_name='work_schedule',
            name='working_from',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='work_schedule',
            name='working_to',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]