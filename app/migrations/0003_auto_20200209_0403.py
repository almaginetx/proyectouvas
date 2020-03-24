# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200207_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300, verbose_name=b'Title')),
                ('color', models.CharField(max_length=300, verbose_name=b'Color')),
                ('description', models.TextField(verbose_name=b'Description', blank=True)),
                ('picture', models.ImageField(null=True, upload_to=b'config', blank=True)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False)),
            ],
            options={
                'ordering': ['create_at'],
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
            },
        ),
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ['create_at'], 'verbose_name': 'Audio', 'verbose_name_plural': 'Audios'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
    ]
