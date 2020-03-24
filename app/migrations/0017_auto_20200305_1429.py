# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='address',
            field=models.CharField(max_length=600, verbose_name=b'Direcci\xc3\xb3n', blank=True),
        ),
        migrations.AddField(
            model_name='date',
            name='map',
            field=models.TextField(verbose_name=b'Google Maps', blank=True),
        ),
    ]
