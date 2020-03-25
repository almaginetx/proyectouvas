# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import app.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_auto_20200324_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.FloatField(default=0, null=True, verbose_name=b'Titled', blank=True)),
                ('code', models.IntegerField(default=app.models.random_string)),
                ('link', models.CharField(default=b'link', max_length=b'1200')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False)),
                ('user', models.ForeignKey(related_name='title_owner', verbose_name=b'Usuario', blank=True, to='app.UserProfile', null=True)),
            ],
            options={
                'ordering': ['create_at'],
                'verbose_name': 'INKACOIN LINK',
                'verbose_name_plural': 'INKACOIN LINKS',
            },
        ),
    ]
