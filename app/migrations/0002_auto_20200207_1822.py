# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300, verbose_name=b'Title')),
                ('description', models.TextField(verbose_name=b'Description', blank=True)),
                ('picture', models.ImageField(null=True, upload_to=b'blogs', blank=True)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False)),
            ],
            options={
                'ordering': ['create_at'],
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300, verbose_name=b'Title')),
                ('description', models.TextField(verbose_name=b'Description', blank=True)),
                ('picture', models.ImageField(null=True, upload_to=b'categories', blank=True)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False)),
            ],
            options={
                'ordering': ['create_at'],
                'verbose_name': 'Tema',
                'verbose_name_plural': 'Temas',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(verbose_name=b'Category-Blog', blank=True, to='app.Category', null=True),
        ),
    ]
