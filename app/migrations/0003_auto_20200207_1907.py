# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200207_1822'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ['create_at'], 'verbose_name': 'Audio', 'verbose_name_plural': 'Audios'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
    ]
