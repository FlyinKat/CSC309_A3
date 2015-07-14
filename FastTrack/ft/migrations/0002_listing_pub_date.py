# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ft', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='pub_date',
            field=models.DateTimeField(default=1, verbose_name='date published'),
            preserve_default=False,
        ),
    ]
