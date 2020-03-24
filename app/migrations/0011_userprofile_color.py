# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200219_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='color',
            field=models.CharField(max_length=200, verbose_name=b'color', blank=True),
        ),
    ]
