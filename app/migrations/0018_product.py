# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20200305_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300, verbose_name=b'Titulo')),
                ('picture', models.ImageField(null=True, upload_to=b'dates', blank=True)),
                ('link', models.CharField(max_length=3000, verbose_name=b'Link', blank=True)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False)),
            ],
            options={
                'ordering': ['create_at'],
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Inventario',
            },
        ),
    ]
