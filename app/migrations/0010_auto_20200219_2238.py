# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='who',
            field=models.TextField(verbose_name=b'Texto Quienes somos', blank=True),
        ),
        migrations.AlterField(
            model_name='config',
            name='description',
            field=models.TextField(verbose_name=b'Descripcion de portada', blank=True),
        ),
        migrations.AlterField(
            model_name='config',
            name='picture',
            field=models.ImageField(upload_to=b'config', null=True, verbose_name=b'Foto de portada', blank=True),
        ),
        migrations.AlterField(
            model_name='config',
            name='title',
            field=models.CharField(max_length=300, verbose_name=b'Titulo'),
        ),
    ]
