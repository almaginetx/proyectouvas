# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200209_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='color',
            field=models.CharField(max_length=300, verbose_name=b'Color', blank=True),
        ),
    ]
