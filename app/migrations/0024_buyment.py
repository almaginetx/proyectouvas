# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20200315_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.IntegerField(default=0, null=True, verbose_name=b'Total a pagar', blank=True)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False)),
                ('buyment', models.ForeignKey(related_name='buyment_owner', verbose_name=b'Usuario', blank=True, to='app.UserProfile', null=True)),
            ],
            options={
                'ordering': ['create_at'],
                'verbose_name': 'Orden de compra',
                'verbose_name_plural': 'Ordenes de compra',
            },
        ),
    ]
