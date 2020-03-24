# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_userprofile_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(verbose_name=b'title', blank=True)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=144, editable=False)),
            ],
            options={
                'ordering': ['create_at'],
                'verbose_name': 'Actualizaci\xf3n',
                'verbose_name_plural': 'Actualizaciones',
            },
        ),
    ]
