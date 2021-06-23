# Generated by Django 3.2.4 on 2021-06-23 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barbershopapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Waitlist_Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershopapi.service')),
                ('waitlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barbershopapi.waitlist')),
            ],
        ),
    ]
