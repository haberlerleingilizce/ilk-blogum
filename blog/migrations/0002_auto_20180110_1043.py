# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-10 07:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='yayınlanma_tarihi',
            new_name='yayinlanma_tarihi',
        ),
    ]
