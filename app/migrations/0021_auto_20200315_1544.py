# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20200314_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boucher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300, verbose_name=b'Codigo')),
                ('description', models.TextField(verbose_name=b'Comentario', blank=True)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False)),
                ('owner', models.ForeignKey(related_name='payment_owner', verbose_name=b'Usuario', blank=True, to='app.UserProfile', null=True)),
            ],
            options={
                'ordering': ['create_at'],
                'verbose_name': 'Recibo de pago',
                'verbose_name_plural': 'Recibos de pago',
            },
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ['create_at'], 'verbose_name': 'Tipo de Pago', 'verbose_name_plural': 'Tipos de Pago'},
        ),
        migrations.AddField(
            model_name='boucher',
            name='payment',
            field=models.ForeignKey(verbose_name=b'Tipo de pago', blank=True, to='app.Payment', null=True),
        ),
    ]
