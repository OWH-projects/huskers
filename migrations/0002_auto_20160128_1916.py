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
            name='offer_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='badges',
            field=models.ManyToManyField(to='huskers.Badge', blank=True),
        ),
    ]
