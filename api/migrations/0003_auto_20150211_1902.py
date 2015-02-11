# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150211_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recording',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
