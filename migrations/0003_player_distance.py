# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('huskers', '0002_auto_20160128_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='distance',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
