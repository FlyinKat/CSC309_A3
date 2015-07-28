# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('courierID', models.CharField(max_length=200)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CourierListing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('courierListingID', models.CharField(max_length=200)),
                ('startLocation', models.CharField(max_length=200)),
                ('endLocation', models.CharField(max_length=200)),
                ('arrivalTime', models.DateTimeField(default=0)),
                ('status', models.BooleanField()),
                ('poster', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('customerID', models.IntegerField(default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerListing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('customerListingID', models.IntegerField(default=0)),
                ('startLocation', models.CharField(max_length=200)),
                ('endLocation', models.CharField(max_length=200)),
                ('arrivalTime', models.DateTimeField(default=0)),
                ('status', models.BooleanField()),
                ('poster', models.ForeignKey(to='ft.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('comment', models.CharField(max_length=200)),
                ('rating', models.IntegerField(default=0)),
                ('courier', models.ForeignKey(to='ft.Courier')),
                ('customer', models.ForeignKey(to='ft.Customer')),
            ],
        ),
    ]
