# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='inkacoin',
            field=models.IntegerField(default=0, null=True, verbose_name=b'Costo Inkacoin en $COP', blank=True),
        ),
        migrations.AddField(
            model_name='config',
            name='maximo',
            field=models.IntegerField(default=0, null=True, verbose_name=b'Costo Maximo Inkacoin en $COP', blank=True),
        ),
        migrations.AddField(
            model_name='config',
            name='minimo',
            field=models.IntegerField(default=0, null=True, verbose_name=b'Costo Minimo Inkacoin en $COP', blank=True),
        ),
    ]
