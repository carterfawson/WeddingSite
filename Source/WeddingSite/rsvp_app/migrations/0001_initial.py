# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('contactid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=30)),
                ('zip', models.CharField(max_length=5)),
                ('phone', models.CharField(max_length=13)),
                ('comments', models.TextField()),
                ('attendees', models.TextField()),
                ('guestnum', models.IntegerField()),
            ],
        ),
    ]
