# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_boucher_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='boucher',
            name='address',
            field=models.CharField(max_length=300, verbose_name=b'Direcci\xc3\xb3n', blank=True),
        ),
        migrations.AddField(
            model_name='boucher',
            name='amount',
            field=models.CharField(max_length=300, verbose_name=b'Monto pagado', blank=True),
        ),
        migrations.AddField(
            model_name='boucher',
            name='name',
            field=models.CharField(max_length=300, verbose_name=b'Nombres y apellidos', blank=True),
        ),
        migrations.AddField(
            model_name='boucher',
            name='tlf',
            field=models.CharField(max_length=300, verbose_name=b'Tel\xc3\xa9fono', blank=True),
        ),
    ]
