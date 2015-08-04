# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_userprofile_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='DENOMINATOR',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='NUMERATOR',
            field=models.IntegerField(default=0),
        ),
    ]
