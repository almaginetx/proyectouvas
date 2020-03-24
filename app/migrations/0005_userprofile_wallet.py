# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200209_0407'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='wallet',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
