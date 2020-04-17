# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pdf',
            field=models.FileField(null=True, upload_to=b'products/pdf', blank=True),
        ),
    ]
