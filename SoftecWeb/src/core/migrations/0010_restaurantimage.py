# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-19 17:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_dataitem_globalpasword'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to=b'')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Restaurant')),
            ],
        ),
    ]
