# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122, unique=True)),
                ('slug', models.SlugField(blank=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=20)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('description', models.TextField()),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='item',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restuarants.Restaurant'),
        ),
    ]
