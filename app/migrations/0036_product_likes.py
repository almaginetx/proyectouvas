# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_product_pdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='likes',
            field=models.IntegerField(default=0, null=True, verbose_name=b'Likes', blank=True),
        ),
    ]
