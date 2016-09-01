# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('huskers', '0003_player_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='profile_link_247',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='player',
            name='profile_link_espn',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='player',
            name='profile_link_rivals',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='player',
            name='profile_link_scout',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
    ]
