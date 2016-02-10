from django.contrib import admin
from models import *

class PlayerAdmin(admin.ModelAdmin):
    list_display = ['player_name', 'year', 'position', 'state', 'status', ]
    list_editable = ['status',]
    search_fields = ['player_name']
    list_filter = ['status', 'year', 'position',]
    filter_horizontal = [ 'badges' ]
    fieldsets = (
        (None, {
            'fields': ('year', 'player_name', ('first_name', 'last_name'), 'position', ('height', 'weight'), ('city', 'state', 'country', 'distance'), 'highschool', 'bio', 'bio_huskers', 'related_features', ('status', 'target_schools', 'transfer_status', 'juco_name'),  'offer_date', 'commit_date', 'decommit_date', 'official_visit_date', 'signed', 'used_redshirt')
        }),
        ('Photos', {
            'fields': ('mugshot', 'feature_photo_credit', 'feature_photo_caption', 'cropped_mug')
        }),
        ('Ratings', {
            'fields': (('stars_247', 'rating_national_247', 'rating_position_247'), ('stars_247c', 'rating_national_247c', 'rating_position_247c'), ('stars_rivals', 'rating_national_rivals', 'rating_position_rivals'), ('stars_scouts', 'rating_national_espn', 'rating_position_espn'), ('stars_fox', 'rating_national_scout', 'rating_position_scout'))
        }),	
        ('Hudl', {
            'fields': ('hudl_title', 'hudl_image', 'hudl_embed', 'hudl_link')
        }),	
        ('Recruiters', {
            'fields': ('recruiter_1', 'recruiter_2')
        }),	
        ('Badges', {
            'fields': ('badges',)
        }),	    
        ('NFL Draft', {
            'fields': ('draft_year', 'draft_team', 'draft_round', 'draft_overall_pick', 'draft_notes',)
        }),
        ('Social media', {
            'fields': ('player_twitter', 'player_instagram',)
        }),		)

class RecruitHeadlineAdmin(admin.ModelAdmin):
    list_display = [ 'hed', 'priority', 'source', 'subscription', 'tags' ]
    ordering = [ '-priority' ]
    list_filter = [ 'tags' ]

class DraftAdmin(admin.ModelAdmin):
    ordering = [ '-year' ]


class DraftTeamAdmin(admin.ModelAdmin):
    ordering = [ 'team_name' ]	
	
	
admin.site.register(Player, PlayerAdmin)
admin.site.register(RecruitHeadline, RecruitHeadlineAdmin)
admin.site.register(Badge)
admin.site.register(Recruiter)
admin.site.register(Draft, DraftAdmin)
admin.site.register(DraftTeam, DraftTeamAdmin)
