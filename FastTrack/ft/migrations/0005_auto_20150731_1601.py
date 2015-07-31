# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ft', '0004_auto_20150731_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='courierlisting',
            name='itemInfo',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customerlisting',
            name='itemInfo',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
