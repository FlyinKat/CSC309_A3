# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ft', '0002_listing_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='pub_date',
        ),
    ]
