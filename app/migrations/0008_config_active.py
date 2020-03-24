# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200209_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='active',
            field=models.IntegerField(default=1, null=True, verbose_name=b'\xc2\xbfActivado?', blank=True),
        ),
    ]
