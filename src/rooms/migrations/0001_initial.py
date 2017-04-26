# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 22:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_title', models.CharField(max_length=200)),
                ('event_start', models.DateField(default=django.utils.timezone.now)),
                ('event_end', models.DateField(blank=True, null=True)),
                ('resource', models.CharField(max_length=20)),
                ('event_type', models.CharField(max_length=30)),
                ('event_color', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]
