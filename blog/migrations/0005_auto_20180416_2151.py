# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-16 18:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180404_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blog.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='app',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blog.App'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='view',
            name='report',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blog.Report'),
            preserve_default=False,
        ),
    ]