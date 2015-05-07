from django.db import models
from django.template.defaultfilters import slugify

stars = (
    ('5 stars', '5 stars'),
    ('4 stars', '4 stars'),
    ('3 stars', '3 stars'),
    ('2 stars', '2 stars'),
    ('1 star', '1 star'),
    ('Unranked', 'Unranked'),
)
    

recruit_status = (
    ('Scholarship', 'Scholarship'),
    ('Walk-on', 'Walk-on'),
    ('Target', 'Target'),
)

class Recruiter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='huskermugs/recruiter/', max_length=100, null=True, blank=True)
    full_name = models.CharField(max_length=100, null=True, blank=True, editable=False)
    nameslug = models.CharField(max_length=100, null=True, blank=True, editable=False)

    def save(self):
        self.full_name = '%s %s' % (self.first_name, self.last_name)
        super(Recruiter, self).save()	
	
    def __unicode__(self):
        return self.full_name

class Draft(models.Model):
    year = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.year

class DraftTeam(models.Model):
    team_name = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    team_name_slug = models.CharField(max_length=100, blank=True, null=True, editable=False)

    def save(self):
        self.team_name_slug = slugify(self.team_name)
        super(DraftTeam, self).save()
    
    def __unicode__(self):
        return self.team_name

		
class Badge(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='huskermugs/badge/', max_length=100, null=True, blank=True)
    internal = models.TextField(blank=True, null=True)
	
    def __unicode__(self):
        return self.name
	
class Player(models.Model):
    year = models.CharField(max_length=4)
    number = models.CharField(max_length=40, null=True, blank=True, editable=False)
    player_name = models.CharField(max_length=100, help_text='Firstname Lastname')
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True, choices=recruit_status)
    mugshot = models.ImageField('Featured Photo', upload_to='huskermugs/', max_length=100, null=True, blank=True)
    feature_photo_credit = models.CharField(max_length=255, null=True, blank=True)
    cropped_mug = models.ImageField('Mugshot', upload_to='huskermugs/', max_length=100, null=True, blank=True)
    position = models.CharField(max_length=75, null=True, blank=True, help_text='Enter QB for quarterback, LB for linebacker, etc.')
    height = models.CharField(max_length=7, blank=True, null=True, help_text='Example: 6/2')
    weight = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    state = models.CharField(max_length=25, null=True, blank=True, help_text='Two-letter abbreviation')
    country = models.CharField(max_length=100, null=True, blank=True, help_text='Non-USA only')
    highschool= models.CharField(max_length=75, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    lastchange = models.DateTimeField(auto_now=True)
    nameslug = models.CharField(max_length=100, null=True, blank=True, editable=False)
    signed = models.BooleanField()
    hudl_title = models.CharField(max_length=300, null=True, blank=True)
    hudl_image = models.ImageField(upload_to='huskermugs/hudl/', max_length=100, null=True, blank=True)
    hudl_embed = models.TextField(null=True, blank=True)
    hudl_link = models.CharField(max_length=300, null=True, blank=True)
    stars_247 = models.CharField('Rating: 247 Sports', max_length=10, null=True, blank=True, choices=stars)
    stars_rivals = models.CharField('Rating: Rivals', max_length=10, null=True, blank=True, choices=stars)
    stars_scouts = models.CharField('Rating: ESPN', max_length=10, null=True, blank=True, choices=stars)
    stars_fox = models.CharField('Rating: Scout.com', max_length=10, null=True, blank=True, choices=stars)
    stars_247c = models.CharField('Rating: 247 Composite', max_length=10, null=True, blank=True, choices=stars)
    target = models.BooleanField()
    target_schools = models.CharField(max_length=150, null=True, blank=True)
    rating_national_247 = models.CharField('247 National', max_length=5, null=True, blank=True)
    rating_position_247 = models.CharField('247 Position', max_length=5, null=True, blank=True)
    rating_national_247c = models.CharField('247C National', max_length=5, null=True, blank=True)
    rating_position_247c = models.CharField('247C Position', max_length=5, null=True, blank=True)
    rating_national_espn = models.CharField('ESPN National', max_length=5, null=True, blank=True)
    rating_position_espn = models.CharField('ESPN Position', max_length=5, null=True, blank=True)
    rating_national_rivals = models.CharField('Rivals National', max_length=5, null=True, blank=True)
    rating_position_rivals = models.CharField('Rivals Position', max_length=5, null=True, blank=True)
    rating_national_scout = models.CharField('Scout National', max_length=5, null=True, blank=True)
    rating_position_scout = models.CharField('Scout Position', max_length=5, null=True, blank=True)
    recruiter_1 = models.ForeignKey(Recruiter, related_name="recruiterone", null=True, blank=True)
    recruiter_2 = models.ForeignKey(Recruiter, related_name="recruitertwo",  null=True, blank=True)
    badges = models.ManyToManyField(Badge, blank=True, null=True)
    draft_year = models.ForeignKey(Draft, null=True, blank=True)
    draft_team = models.ForeignKey(DraftTeam, null=True, blank=True)
    draft_round = models.CharField(max_length=100, null=True, blank=True)
    draft_overall_pick = models.PositiveIntegerField(null=True, blank=True)
    draft_notes = models.TextField(null=True, blank=True)
	
    def save(self):
        self.nameslug = slugify(self.player_name)
        super(Player, self).save()

    def __unicode__(self):
        return self.player_name

class RecruitHeadline(models.Model):
    hed = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='huskers/headline-photos/', max_length=100, null=True, blank=True)
    link = models.CharField(max_length=200, null=True, blank=True)
    subscription = models.BooleanField(help_text='Check box if subscription is required to read the article.')
    source = models.CharField(max_length=100, blank=True, help_text="Name of source, i.e. \'Chicago Tribune\'")
    tags = models.CharField(max_length=150, blank=True, help_text="Lowercase. Use hyphens instead of spaces. Examples: recruiting, tommie-frazier, signing-day-2013")
    date = models.DateField(blank=True, null=True)
    priority = models.PositiveIntegerField(help_text="Used for ordering multiple items on the same day. 1 is first, 2 is second, etc.", blank=True)
    
