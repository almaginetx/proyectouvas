# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_wallet'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wallet',
            options={'ordering': ['create_at'], 'verbose_name': 'INKACOIN Wallet', 'verbose_name_plural': 'INKACOIN Wallets'},
        ),
    ]
