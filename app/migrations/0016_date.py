# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_company_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300, verbose_name=b'Titulo')),
                ('description', models.TextField(verbose_name=b'Descripci\xc3\xb3n', blank=True)),
                ('picture', models.ImageField(null=True, upload_to=b'dates', blank=True)),
                ('start', models.DateTimeField(null=True, blank=True)),
                ('finish', models.DateTimeField(null=True, blank=True)),
                ('active', models.IntegerField(default=0, null=True, verbose_name=b'\xc2\xbfPrincipal?', blank=True)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False)),
                ('owner', models.ForeignKey(related_name='evento_owner', verbose_name=b'Usuario', blank=True, to='app.UserProfile', null=True)),
            ],
            options={
                'ordering': ['create_at'],
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
    ]
