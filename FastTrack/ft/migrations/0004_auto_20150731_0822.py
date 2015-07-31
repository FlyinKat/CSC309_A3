# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ft', '0003_auto_20150730_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courierlisting',
            name='poster',
            field=models.ForeignKey(to='ft.Courier', null=True),
        ),
    ]
