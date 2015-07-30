# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ft', '0002_auto_20150729_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courierlisting',
            name='courierListingID',
            field=models.IntegerField(default=0),
        ),
    ]
