# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20200315_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cant', models.IntegerField(default=0, null=True, verbose_name=b'Cantidad', blank=True)),
                ('price', models.FloatField(default=0, null=True, verbose_name=b'Costo', blank=True)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False)),
                ('owner', models.ForeignKey(related_name='cart_owner', verbose_name=b'Usuario', blank=True, to='app.UserProfile', null=True)),
                ('product', models.ForeignKey(verbose_name=b'Producto', blank=True, to='app.Product', null=True)),
            ],
            options={
                'ordering': ['create_at'],
                'verbose_name': 'Articulos en carritos',
                'verbose_name_plural': 'Carritos de compra',
            },
        ),
    ]
