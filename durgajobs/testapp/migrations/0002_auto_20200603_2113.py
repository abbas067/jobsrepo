# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-06-03 15:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blorejobs',
            old_name='eiigibility',
            new_name='eligibility',
        ),
        migrations.RenameField(
            model_name='hydjobs',
            old_name='eiigibility',
            new_name='eligibility',
        ),
        migrations.RenameField(
            model_name='punejobs',
            old_name='eiigibility',
            new_name='eligibility',
        ),
    ]