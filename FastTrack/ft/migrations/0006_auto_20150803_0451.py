# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ft', '0005_auto_20150731_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courierlisting',
            name='arrivalTime',
            field=models.TimeField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='customerlisting',
            name='arrivalTime',
            field=models.TimeField(default=0, null=True),
        ),
    ]
