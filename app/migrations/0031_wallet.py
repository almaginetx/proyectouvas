# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import app.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_userprofile_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.FloatField(default=0, null=True, verbose_name=b'Wallet', blank=True)),
                ('code', models.CharField(default=app.models.random_string, max_length=100)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False)),
                ('user', models.ForeignKey(related_name='wallet_owner', verbose_name=b'Usuario', blank=True, to='app.UserProfile', null=True)),
            ],
            options={
                'ordering': ['create_at'],
                'verbose_name': 'Orden de compra',
                'verbose_name_plural': 'Ordenes de compra',
            },
        ),
    ]
