# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='verified',
            field=models.IntegerField(default=0, null=True, verbose_name=b'\xc2\xbfVerificado?', blank=True),
        ),
    ]
