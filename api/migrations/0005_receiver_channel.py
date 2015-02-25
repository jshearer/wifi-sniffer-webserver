# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_host_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiver',
            name='channel',
            field=models.IntegerField(default=6, null=True),
            preserve_default=True,
        ),
    ]
