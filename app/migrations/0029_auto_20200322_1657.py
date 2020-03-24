# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20200315_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name=b'Description', blank=True),
        ),
    ]
