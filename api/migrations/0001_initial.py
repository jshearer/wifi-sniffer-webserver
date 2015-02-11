# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalculatedPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('uncertainty', models.FloatField()),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('z', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=400)),
                ('device_uid', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mac_addr', models.CharField(max_length=100)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('z', models.FloatField()),
                ('host', models.ForeignKey(to='api.Host')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recording',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rssi', models.FloatField()),
                ('data', models.CharField(max_length=1000, null=True)),
                ('time', models.DateTimeField()),
                ('receiver', models.ForeignKey(to='api.Receiver')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transmitter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mac_addr', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WifiSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enabled', models.BooleanField(default=True)),
                ('ESSID', models.CharField(max_length=100)),
                ('security', models.CharField(default=b'none', max_length=20)),
                ('ip', models.CharField(default=b'dhcp', max_length=100)),
                ('key', models.CharField(max_length=400, null=True)),
                ('hidden', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='recording',
            name='transmitter',
            field=models.ForeignKey(to='api.Transmitter'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='wifi_settings',
            field=models.ForeignKey(to='api.WifiSettings'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='location',
            field=models.ForeignKey(to='api.Location'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='calculatedposition',
            name='transmitter',
            field=models.ForeignKey(to='api.Transmitter'),
            preserve_default=True,
        ),
    ]
