# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=16, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=16)),
                ('phone', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=16)),
                ('body_id', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
