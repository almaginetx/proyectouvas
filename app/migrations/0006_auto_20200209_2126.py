# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_userprofile_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='address',
            field=models.CharField(max_length=300, verbose_name=b'Direcci\xc3\xb3n', blank=True),
        ),
        migrations.AddField(
            model_name='config',
            name='map',
            field=models.TextField(verbose_name=b'Mapa de google', blank=True),
        ),
        migrations.AddField(
            model_name='config',
            name='tlf',
            field=models.CharField(max_length=300, verbose_name=b'Tel\xc3\xa9fono', blank=True),
        ),
    ]
