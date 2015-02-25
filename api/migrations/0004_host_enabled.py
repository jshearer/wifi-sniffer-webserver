# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150211_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='enabled',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
