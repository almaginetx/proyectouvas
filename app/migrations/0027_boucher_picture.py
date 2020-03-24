# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='boucher',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'payments', blank=True),
        ),
    ]
