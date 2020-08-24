# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.IntegerField(default=0, null=True, verbose_name=b'Likes', blank=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(related_name='blog_owner', verbose_name=b'Usuario', blank=True, to='app.UserProfile', null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='views',
            field=models.IntegerField(default=0, null=True, verbose_name=b'views', blank=True),
        ),
    ]
