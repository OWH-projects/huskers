# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('notes', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'huskermugs/badge/', blank=True)),
                ('internal', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Draft',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.CharField(max_length=100)),
                ('notes', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='DraftTeam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_name', models.CharField(max_length=100)),
                ('notes', models.TextField(null=True, blank=True)),
                ('team_name_slug', models.CharField(max_length=100, null=True, editable=False, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.CharField(max_length=4)),
                ('number', models.CharField(max_length=40, null=True, editable=False, blank=True)),
                ('player_name', models.CharField(help_text=b'Firstname Lastname', max_length=100)),
                ('first_name', models.CharField(max_length=100, null=True, blank=True)),
                ('last_name', models.CharField(max_length=100, blank=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True, choices=[(b'Scholarship', b'Scholarship'), (b'Walk-on', b'Walk-on'), (b'Target', b'Target'), (b'Decommit', b'Decommit')])),
                ('mugshot', models.ImageField(upload_to=b'huskermugs/', null=True, verbose_name=b'Featured Photo', blank=True)),
                ('feature_photo_credit', models.CharField(max_length=255, null=True, blank=True)),
                ('cropped_mug', models.ImageField(upload_to=b'huskermugs/', null=True, verbose_name=b'Mugshot', blank=True)),
                ('position', models.CharField(help_text=b'Enter QB for quarterback, LB for linebacker, etc.', max_length=75, null=True, blank=True)),
                ('height', models.CharField(help_text=b'Example: 6/2', max_length=7, null=True, blank=True)),
                ('weight', models.IntegerField(null=True, blank=True)),
                ('city', models.CharField(max_length=40, null=True, blank=True)),
                ('state', models.CharField(help_text=b'Two-letter abbreviation', max_length=25, null=True, blank=True)),
                ('country', models.CharField(help_text=b'Non-USA only', max_length=100, null=True, blank=True)),
                ('highschool', models.CharField(max_length=75, null=True, blank=True)),
                ('bio', models.TextField(null=True, blank=True)),
                ('lastchange', models.DateTimeField(auto_now=True)),
                ('nameslug', models.CharField(max_length=100, null=True, editable=False, blank=True)),
                ('signed', models.BooleanField()),
                ('hudl_title', models.CharField(max_length=300, null=True, blank=True)),
                ('hudl_image', models.ImageField(null=True, upload_to=b'huskermugs/hudl/', blank=True)),
                ('hudl_embed', models.TextField(null=True, blank=True)),
                ('hudl_link', models.CharField(max_length=300, null=True, blank=True)),
                ('stars_247', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'Rating: 247 Sports', choices=[(b'5 stars', b'5 stars'), (b'4 stars', b'4 stars'), (b'3 stars', b'3 stars'), (b'2 stars', b'2 stars'), (b'1 star', b'1 star'), (b'Unranked', b'Unranked')])),
                ('stars_rivals', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'Rating: Rivals', choices=[(b'5 stars', b'5 stars'), (b'4 stars', b'4 stars'), (b'3 stars', b'3 stars'), (b'2 stars', b'2 stars'), (b'1 star', b'1 star'), (b'Unranked', b'Unranked')])),
                ('stars_scouts', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'Rating: ESPN', choices=[(b'5 stars', b'5 stars'), (b'4 stars', b'4 stars'), (b'3 stars', b'3 stars'), (b'2 stars', b'2 stars'), (b'1 star', b'1 star'), (b'Unranked', b'Unranked')])),
                ('stars_fox', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'Rating: Scout.com', choices=[(b'5 stars', b'5 stars'), (b'4 stars', b'4 stars'), (b'3 stars', b'3 stars'), (b'2 stars', b'2 stars'), (b'1 star', b'1 star'), (b'Unranked', b'Unranked')])),
                ('stars_247c', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'Rating: 247 Composite', choices=[(b'5 stars', b'5 stars'), (b'4 stars', b'4 stars'), (b'3 stars', b'3 stars'), (b'2 stars', b'2 stars'), (b'1 star', b'1 star'), (b'Unranked', b'Unranked')])),
                ('target', models.BooleanField()),
                ('target_schools', models.CharField(max_length=150, null=True, blank=True)),
                ('rating_national_247', models.CharField(max_length=5, null=True, verbose_name=b'247 National', blank=True)),
                ('rating_position_247', models.CharField(max_length=5, null=True, verbose_name=b'247 Position', blank=True)),
                ('rating_national_247c', models.CharField(max_length=5, null=True, verbose_name=b'247C National', blank=True)),
                ('rating_position_247c', models.CharField(max_length=5, null=True, verbose_name=b'247C Position', blank=True)),
                ('rating_national_espn', models.CharField(max_length=5, null=True, verbose_name=b'ESPN National', blank=True)),
                ('rating_position_espn', models.CharField(max_length=5, null=True, verbose_name=b'ESPN Position', blank=True)),
                ('rating_national_rivals', models.CharField(max_length=5, null=True, verbose_name=b'Rivals National', blank=True)),
                ('rating_position_rivals', models.CharField(max_length=5, null=True, verbose_name=b'Rivals Position', blank=True)),
                ('rating_national_scout', models.CharField(max_length=5, null=True, verbose_name=b'Scout National', blank=True)),
                ('rating_position_scout', models.CharField(max_length=5, null=True, verbose_name=b'Scout Position', blank=True)),
                ('draft_round', models.CharField(max_length=100, null=True, blank=True)),
                ('draft_overall_pick', models.PositiveIntegerField(null=True, blank=True)),
                ('draft_notes', models.TextField(null=True, blank=True)),
                ('badges', models.ManyToManyField(to='huskers.Badge', null=True, blank=True)),
                ('draft_team', models.ForeignKey(blank=True, to='huskers.DraftTeam', null=True)),
                ('draft_year', models.ForeignKey(blank=True, to='huskers.Draft', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('notes', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'huskermugs/recruiter/', blank=True)),
                ('full_name', models.CharField(max_length=100, null=True, editable=False, blank=True)),
                ('nameslug', models.CharField(max_length=100, null=True, editable=False, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecruitHeadline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hed', models.CharField(max_length=100)),
                ('body', models.TextField(null=True, blank=True)),
                ('photo', models.ImageField(null=True, upload_to=b'huskers/headline-photos/', blank=True)),
                ('link', models.CharField(max_length=200, null=True, blank=True)),
                ('subscription', models.BooleanField(help_text=b'Check box if subscription is required to read the article.')),
                ('source', models.CharField(help_text=b"Name of source, i.e. 'Chicago Tribune'", max_length=100, blank=True)),
                ('tags', models.CharField(help_text=b'Lowercase. Use hyphens instead of spaces. Examples: recruiting, tommie-frazier, signing-day-2013', max_length=150, blank=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('priority', models.PositiveIntegerField(help_text=b'Used for ordering multiple items on the same day. 1 is first, 2 is second, etc.', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='recruiter_1',
            field=models.ForeignKey(related_name='recruiterone', blank=True, to='huskers.Recruiter', null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='recruiter_2',
            field=models.ForeignKey(related_name='recruitertwo', blank=True, to='huskers.Recruiter', null=True),
        ),
    ]
