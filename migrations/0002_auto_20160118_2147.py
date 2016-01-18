# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('huskers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='feature_photo_caption',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='player',
            name='player_instagram',
            field=models.CharField(help_text=b'Username only. No @ symbol.', max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='player',
            name='player_twitter',
            field=models.CharField(help_text=b'Username only. No @ symbol.', max_length=100, null=True, blank=True),
        ),
    ]
