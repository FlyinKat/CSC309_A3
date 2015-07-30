# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ft', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courierlisting',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customerlisting',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
