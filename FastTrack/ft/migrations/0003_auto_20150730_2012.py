# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ft', '0002_auto_20150730_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerlisting',
            name='poster',
            field=models.ForeignKey(null=True, to='ft.Customer'),
        ),
    ]
