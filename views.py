from models import *
from django.shortcuts import *
from django.db.models import *

years = Player.objects.all().values('year').distinct().order_by('-year')
states = Player.objects.all().values('state').distinct().order_by('state')


# All of the Signing Day pages

def Signing(request):
    recentlist = Player.objects.all().filter(year='2011').order_by('-lastchange')
    topschools = Player.objects.all().values('highschool', 'city').annotate(schoolcount=Count('highschool')).order_by('-schoolcount')[:10]
    yearlist = Player.objects.all().values('year').distinct()
    topschoolcount = topschools[0]
    headline = RecruitHeadline.objects.all()[:1]

    dictionaries = { 'headline':headline, 'recentlist': recentlist, 'topschools': topschools, 'topschoolcount': topschoolcount, 'yearlist': yearlist, }
    return render_to_response('huskers/signing-day-2011.html', dictionaries)

def Signing2012(request):
    recentlist = Player.objects.all().filter(status='Scholarship').filter(year='2012').order_by('last_name')
    headline = RecruitHeadline.objects.all()[1:2]

    dictionaries = { 'headline':headline, 'recentlist': recentlist, }
    return render_to_response('huskers/signing-day-2012.html', dictionaries)

def Signing2013(request):
    recentlist = Player.objects.all().filter(status='Scholarship').filter(year='2013').order_by('last_name')
    headline = RecruitHeadline.objects.filter(tags__icontains='signing-day-2013')
    video = RecruitHeadline.objects.filter(tags__icontains='signing-day-video-2013')
    rankings = RecruitHeadline.objects.filter(tags__icontains='signing-day-rankings-2013')

    dictionaries = { 'headline':headline, 'recentlist': recentlist, 'video': video, 'rankings': rankings, }
    return render_to_response('huskers/signing-day-2013.html', dictionaries)

def Signing2014(request):
    recentlist = Player.objects.all().filter(status='Scholarship').filter(year='2014').order_by('last_name')
    headline = RecruitHeadline.objects.filter(tags__icontains='signing-day-2014').order_by('-priority')
    video = RecruitHeadline.objects.filter(tags__icontains='signing-day-video-2014')
    rankings = RecruitHeadline.objects.filter(tags__icontains='signing-day-rankings-2014')
    photos = RecruitHeadline.objects.filter(tags__icontains='signing-day-photos-2014')
    schedule = RecruitHeadline.objects.filter(tags__icontains='signing-day-schedule-2014')
	
    dictionaries = { 'headline':headline, 'recentlist': recentlist, 'video': video, 'rankings': rankings, 'photos': photos, 'schedule': schedule, }
    return render_to_response('huskers/signing-day-2014.html', dictionaries)

def Signing2015(request):
    recentlist = Player.objects.all().filter(status='Scholarship').filter(year='2015').order_by('last_name')
    headline = RecruitHeadline.objects.filter(tags__icontains='signing-day-2015').order_by('-priority')
    top_story = RecruitHeadline.objects.filter(tags__icontains='signing-day-2015-top-story').order_by('-priority')
    video = RecruitHeadline.objects.filter(tags__icontains='signing-day-video-2015').order_by('-priority')
    top_video = RecruitHeadline.objects.filter(tags__icontains='signing-day-video-2015-main').order_by('-priority')[:1]
    rankings = RecruitHeadline.objects.filter(tags__icontains='signing-day-rankings-2015')
    photos = RecruitHeadline.objects.filter(tags__icontains='signing-day-photos-2015')
    schedule = RecruitHeadline.objects.filter(tags__icontains='signing-day-schedule-2015')
	
    dictionaries = { 'headline':headline, 'top_story': top_story, 'recentlist': recentlist, 'video': video, 'top_video': top_video, 'rankings': rankings, 'photos': photos, 'schedule': schedule, }
    return render_to_response('huskers/signing-day-2015.html', dictionaries)


def Signing2016(request):
    recentlist = Player.objects.all().filter(status='Scholarship').filter(year='2016').exclude(transfer_status='University').order_by('last_name')
    headline = RecruitHeadline.objects.filter(tags__icontains='signing-day-2016').exclude(tags__icontains='signing-day-2016-top-story').order_by('-priority')
    top_story = RecruitHeadline.objects.filter(tags__icontains='signing-day-2016-top-story').order_by('-priority')
    video = RecruitHeadline.objects.filter(tags__icontains='signing-day-video-2016').order_by('-priority')
    top_video = RecruitHeadline.objects.filter(tags__icontains='signing-day-video-2016-main').order_by('-priority')[:1]
    rankings = RecruitHeadline.objects.filter(tags__icontains='signing-day-rankings-2016')
    photos = RecruitHeadline.objects.filter(tags__icontains='signing-day-photos-2016')
    schedule = RecruitHeadline.objects.filter(tags__icontains='signing-day-schedule-2016')
    story_count = headline.count() + 1
	
    dictionaries = { 'headline':headline, 'top_story': top_story, 'recentlist': recentlist, 'video': video, 'top_video': top_video, 'rankings': rankings, 'photos': photos, 'schedule': schedule, 'story_count': story_count, }
    return render_to_response('huskers/signing-day-2016.html', dictionaries)




def Splash(request):
    recentlist = Player.objects.all().filter(status='Scholarship').filter(year='2014').order_by('-lastchange')

    dictionaries = { 'recentlist': recentlist, }
    return render_to_response('huskers/signing-day-splash.html', dictionaries)



def YearXML(request, year):
    statelist = Player.objects.filter(year=year).values('state').filter(Q(status='Scholarship') | Q(status__isnull=True)).exclude(transfer_status='University').annotate(statecount=Count('state'))

    return render_to_response('huskers/main.xml', { "statelist": statelist, }, mimetype="application/xhtml+xml")

def StateXML(request):
    statelist = Player.objects.all().values('state').filter(Q(status='Scholarship') | Q(status__isnull=True)).exclude(transfer_status='University').annotate(statecount=Count('state'))

    return render_to_response('huskers/main.xml', { "statelist": statelist, }, mimetype="application/xhtml+xml")

	
def AllYears(request):
    allyears = Player.objects.filter(Q(status='Scholarship') | Q(status__isnull=True)).order_by('-year').values('year').annotate(scholarshipcount=Count('year'))
    walkons = Player.objects.filter(status='Walk-on').order_by('-year').values('year').annotate(walkoncount=Count('year'))
    transfers = Player.objects.filter(transfer_status='University').order_by('-year').values('year').annotate(transfercount=Count('year'))
    return render_to_response('huskers/years-all.html', { "allyears": allyears, "walkons": walkons, "transfers": transfers, })
   	
	
def Year(request, year):
    title = year
    scholarships = Player.objects.filter(year=year).filter(Q(status__isnull=True) | Q(status="Scholarship")).exclude(transfer_status='University').order_by("last_name", "first_name")
    ratings = scholarships.aggregate(two_star=Sum(Case(When(stars_247c="2 stars", then=1),output_field=IntegerField())), three_star=Sum(Case(When(stars_247c="3 stars", then=1),output_field=IntegerField())), four_star=Sum(Case(When(stars_247c="4 stars", then=1),output_field=IntegerField())), five_star=Sum(Case(When(stars_247c="5 stars", then=1),output_field=IntegerField())))
    walkons = Player.objects.filter(year=year).filter(status="Walk-on").order_by("last_name", "first_name")
    transfers = Player.objects.filter(year=year).filter(transfer_status="University").order_by("last_name", "first_name")
    targets = Player.objects.filter(year=year).filter(status="Target").order_by("last_name", "first_name")
	
    return render_to_response('huskers/yearpage2.html', { "title": title, "scholarships": scholarships, "walkons": walkons, "targets": targets, "years": years, "states": states, "ratings": ratings, "transfers": transfers, })



#def State(request, state):
#    title = state
#    statelist = Player.objects.filter(state=state).order_by('-year', 'last_name')
#    playercount = Player.objects.filter(state=state).filter(Q(status='Scholarship') | Q(status__isnull=True)).aggregate(statecount=Count('id'))

#    return render_to_response('huskers/statepage.html',  { "title": title, "statelist": statelist, "playercount": playercount,  "years": years, "states": states, })


def StateMap(request):
    statelist = Player.objects.all().values('state').filter(Q(status='Scholarship') | Q(status__isnull=True)).exclude(transfer_status='University').annotate(statecount=Count('state'))

    return render_to_response('huskers/state-map.js', { "statelist": statelist, })


def State2(request, state):
    title = state
    players = Player.objects.filter(state=state).exclude(status="Target").order_by('last_name', 'first_name')
    scholarships = players.filter(status="Scholarship")
    walkons = players.filter(status="Walk-on")
    transfers = players.filter(transfer_status="University")
    positions = players.values("position").distinct().annotate(positioncount=Count('position')).order_by('-positioncount')

    return render_to_response('huskers/statepage2.html',  { "title": title, "players": players, "scholarships": scholarships, "walkons": walkons, 'positions': positions,  "years": years, "states": states, "transfers": transfers, })

def AllStates(request):
    scholarships = Player.objects.filter(status="Scholarship").order_by('state').values('state').annotate(statecount=Count('state'))
    transfers = Player.objects.filter(transfer_status="University").order_by('state').values('state').annotate(transfercount=Count('state'))
    walkons = Player.objects.filter(status="Walk-on").order_by('state').values('state').annotate(walkoncount=Count('state'))
    return render_to_response('huskers/states-all.html', { "scholarships": scholarships, "walkons": walkons, "transfers": transfers, })	
	
	
	
#def Search(request):
#    query = request.GET.get('q', '')
#    if query:
#        qset = (
#            Q(player_name__icontains=query)
#        )
#        results = Player.objects.filter(qset)
#    else:
#        results = []
#    return render_to_response("huskers/search.html", {
#        "results": results,
#        "query": query,
#    })

def Search2(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(player_name__icontains=query)
        )
        results = Player.objects.filter(qset)
    else:
        results = []
    return render_to_response("huskers/search-new.html", {
        "results": results,
        "query": query,
		"years": years, 
		"states": states, 
    })
	
def PlayerPage(request, playername):
    player = Player.objects.get(nameslug=playername)
    yearlist = Player.objects.all().values('year').distinct().order_by('-year')
    same_year = Player.objects.filter(year=player.year).exclude(status="Target").order_by('-year')[:10]
    same_position = Player.objects.filter(position=player.position).exclude(status="Target").order_by('-year')[:10]
    same_state = Player.objects.filter(state=player.state).exclude(status="Target").order_by('-year')[:10]
    
    return render_to_response('huskers/player2.html', { "player": player, "yearlist": yearlist, "same_position": same_position, "same_year": same_year, "same_state": same_state,  "years": years, "states": states, })	
	

def Recruiting(request):
    recentlist = Player.objects.all().filter(year='2016').exclude(transfer_status="University").order_by('last_name', 'first_name')
    headlines = RecruitHeadline.objects.filter(tags__icontains='recruiting').order_by('priority').order_by('-priority')[:15]
    topschools = Player.objects.all().values('highschool', 'city').annotate(schoolcount=Count('highschool')).order_by('-schoolcount')[:10]
    topschoolcount = topschools[0]
    yearlist = Player.objects.all().values('year').distinct().order_by('-year')

    dictionaries = { 'recentlist': recentlist, 'headlines': headlines, 'topschools': topschools, 'topschoolcount': topschoolcount, 'yearlist': yearlist, }
    return render_to_response('huskers/recruiting.html', dictionaries)
	
	
def RecruitingWidget(request):
    headlines = RecruitHeadline.objects.filter(tags__icontains='recruiting').order_by('priority').order_by('-priority')[:1]

    dictionaries = { 'headlines': headlines, }
    return render_to_response('huskers/recruiting-widget.html', dictionaries)
	
def TargetsSam(request, year):
    targets = Player.objects.all().filter(year=year).order_by('last_name')
    year = year

    dictionaries = { 'targets': targets, 'year': year, }
    return render_to_response('huskers/targets-sam.html', dictionaries)

def Targets(request, year):
    targets = Player.objects.all().filter(year=year).order_by('last_name', 'first_name')
    year = year

    dictionaries = { 'targets': targets, 'year': year,  "years": years, "states": states, }
    return render_to_response('huskers/targets.html', dictionaries)	
	
def DraftPicks(request):
    all_picks = Player.objects.all().filter(draft_year__isnull=False).order_by('-draft_year__year', 'draft_overall_pick')

    dictionaries = { 'all_picks': all_picks, }
    return render_to_response('huskers/draft-all.html', dictionaries)	
	
def DraftSingleTeam(request, slug):
    team = DraftTeam.objects.get(team_name_slug=slug)
    players = Player.objects.filter(draft_team__isnull=False).filter(draft_team__team_name_slug=slug).order_by('-draft_year__year', 'draft_overall_pick')

    dictionaries = { 'team': team, 'players': players, }
    return render_to_response('huskers/draft-team.html', dictionaries)

def DraftSingleYear(request, year):
    year = Draft.objects.get(year=year)
    players = Player.objects.filter(draft_team__isnull=False).filter(draft_year__year=year).order_by('-draft_year__year', 'draft_overall_pick')

    dictionaries = { 'year': year, 'players': players, }
    return render_to_response('huskers/draft-year.html', dictionaries)		

def BadgesAll(request):
    badges = Badge.objects.all().order_by('name')

    dictionaries = { 'badges': badges, }
    return render_to_response('huskers/badges-all.html', dictionaries)

def BadgesSingle(request, nameslug):
    this_badge = Badge.objects.get(nameslug=nameslug)
    players = Player.objects.filter(badges__nameslug=nameslug)

    dictionaries = { 'this_badge': this_badge, 'players': players, }
    return render_to_response('huskers/badges-single.html', dictionaries)	

def Recruiters(request):
    list = Recruiter.objects.all().order_by('last_name')
    for coach in list:
	    coach.player_count = Player.objects.filter(status="Scholarship").filter(Q(recruiter_1__nameslug=coach.nameslug) | Q(recruiter_2__nameslug=coach.nameslug)).count()

    dictionaries = { 'list': list, }
    return render_to_response('huskers/recruiter-all.html', dictionaries)

def RecruiterSingle(request, nameslug):
    this_recruiter = Recruiter.objects.get(nameslug=nameslug)
    players = Player.objects.filter(status="Scholarship").filter(Q(recruiter_1__nameslug=nameslug) | Q(recruiter_2__nameslug=nameslug)).order_by('-year')

    dictionaries = { 'this_recruiter': this_recruiter, 'players': players, }
    return render_to_response('huskers/recruiter-single.html', dictionaries)	