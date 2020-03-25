# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20200324_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='code',
            field=models.IntegerField(default=app.models.random_string),
        ),
    ]
