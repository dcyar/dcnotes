# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 23:22
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('priority', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10)])),
                ('state', models.BooleanField(default=False)),
                ('dateInitial', models.DateField(auto_now_add=True)),
                ('dateEnd', models.DateField()),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
        ),
    ]
