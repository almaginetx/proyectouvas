# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_auto_20200519_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False)),
                ('friend', models.ForeignKey(related_name='friend', verbose_name=b'Amigo', blank=True, to='app.UserProfile', null=True)),
                ('friendof', models.ForeignKey(related_name='friendof', verbose_name=b'Amigo de', blank=True, to='app.UserProfile', null=True)),
            ],
            options={
                'ordering': ['create_at'],
                'verbose_name': 'Lista de amigos',
                'verbose_name_plural': 'Listas de amigos',
            },
        ),
    ]
