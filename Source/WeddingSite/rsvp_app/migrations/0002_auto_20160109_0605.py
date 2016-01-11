# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='advice',
            fields=[
                ('adviceid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('advice', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='attendees',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.CharField(null=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='comments',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(null=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='guestnum',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(null=True, max_length=13),
        ),
        migrations.AlterField(
            model_name='contact',
            name='state',
            field=models.CharField(null=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='zip',
            field=models.CharField(null=True, max_length=5),
        ),
    ]
