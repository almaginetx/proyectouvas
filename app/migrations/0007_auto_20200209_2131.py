# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200209_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='whatsapp',
            field=models.CharField(max_length=300, verbose_name=b'Whatsapp', blank=True),
        ),
        migrations.AlterField(
            model_name='config',
            name='tlf',
            field=models.CharField(max_length=300, verbose_name=b'Texto de Tel\xc3\xa9fono', blank=True),
        ),
    ]
