# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='price',
            field=models.IntegerField(default=0, null=True, verbose_name=b'Costo', blank=True),
        ),
    ]
