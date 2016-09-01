# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('huskers', '0004_auto_20160328_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='announcement_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='player',
            name='committed_school',
            field=models.CharField(blank=True, max_length=200, choices=[(b'Alabama', b'Alabama'), (b'Alaska', b'Alaska')]),
        ),
        migrations.AddField(
            model_name='player',
            name='hard_commit_elsewhere',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='top_target',
            field=models.BooleanField(default=False),
        ),
    ]
