# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='account',
            field=models.CharField(max_length=300, verbose_name=b'Numero de cuenta', blank=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='accunttype',
            field=models.CharField(max_length=300, verbose_name=b'Tipo de cuenta', blank=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='address',
            field=models.CharField(max_length=300, verbose_name=b'Direccion', blank=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='country',
            field=models.CharField(max_length=300, verbose_name=b'Pais', blank=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='description',
            field=models.TextField(verbose_name=b'Notas adicionales', blank=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='govermentid',
            field=models.CharField(max_length=300, verbose_name=b'Identificacion', blank=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='link',
            field=models.CharField(max_length=300, verbose_name=b'Link', blank=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='mail',
            field=models.CharField(max_length=300, verbose_name=b'Email', blank=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='name',
            field=models.CharField(max_length=300, verbose_name=b'Titular', blank=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='phone',
            field=models.CharField(max_length=300, verbose_name=b'Telefono', blank=True),
        ),
    ]
