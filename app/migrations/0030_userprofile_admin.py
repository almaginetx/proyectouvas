# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_auto_20200322_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='admin',
            field=models.IntegerField(default=0, null=True, verbose_name=b'\xc2\xbfAdministrador?', blank=True),
        ),
    ]
