# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-18 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20170817_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whitelabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.CharField(blank=True, max_length=255, null=True)),
                ('primary_domain', models.CharField(max_length=256)),
            ],
        ),
    ]
