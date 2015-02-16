# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('username', models.CharField(max_length=64, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('modify_password', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BaseInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zodiac_year', models.CharField(max_length=16)),
                ('deadline', models.CharField(max_length=64)),
                ('tema_odds', models.IntegerField()),
                ('off_percent', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LotteryUser',
            fields=[
                ('username', models.CharField(max_length=64, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('pay_password', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=32)),
                ('body_id', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=128)),
                ('user_type', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('create_date', models.CharField(max_length=64)),
                ('remark', models.TextField(null=True, blank=True)),
                ('off_percent', models.IntegerField()),
                ('deposit', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.CharField(max_length=128, serialize=False, primary_key=True)),
                ('data', models.TextField()),
                ('win_data', models.TextField(null=True, blank=True)),
                ('buy_amount', models.IntegerField()),
                ('win_amount', models.IntegerField()),
                ('net_amount', models.IntegerField()),
                ('buy_time', models.CharField(max_length=64)),
                ('status', models.CharField(max_length=16)),
                ('remark', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('round_id', models.CharField(max_length=128, serialize=False, primary_key=True)),
                ('round_th', models.IntegerField()),
                ('open_time', models.CharField(max_length=64)),
                ('colse_time', models.CharField(max_length=64)),
                ('result_time', models.CharField(max_length=64)),
                ('pingma', models.CharField(max_length=16)),
                ('tema', models.CharField(max_length=4)),
                ('status', models.CharField(max_length=16)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='order',
            name='round_id',
            field=models.ForeignKey(to='lottery.Round'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='username',
            field=models.ForeignKey(to='lottery.LotteryUser'),
            preserve_default=True,
        ),
    ]
