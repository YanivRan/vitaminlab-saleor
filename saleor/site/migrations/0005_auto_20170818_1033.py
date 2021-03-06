# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-18 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0004_auto_20170221_0426'),
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
        migrations.AlterField(
            model_name='authorizationkey',
            name='name',
            field=models.CharField(choices=[('facebook', 'Facebook-Oauth2'), ('google-oauth2', 'Google-Oauth2')], max_length=20, verbose_name='name'),
        ),
    ]
