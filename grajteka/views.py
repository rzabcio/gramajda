# Create your views here.

import django
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic.list_detail import object_list

from grajteka.models import *
from grajteka.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,user_passes_test

def index(request):
	return render_to_response('index.html',
		{'version':django.VERSION},
		context_instance=RequestContext(request))

def boardgames_list(request):
	boardgames = Boardgame.objects.all().order_by("meta__title")
        return object_list(
                request,
                boardgames,
                paginate_by=20,
                extra_context={},
		template_name='boardgames_list.html')


def boardgame_view(request,boardgameid):
	b = Boardgame.objects.get(id=boardgameid)
	users = User.objects.all().order_by('username')
	users_as_table = ''
	for u in users:
		users_as_table += '"' + u.username + '", '
	transfer_form = TransferForm(initial={'boardgame_id':boardgameid})
	transfers = Transfer.objects.filter(boardgame=b)
	return render_to_response('boardgame_view.html',
		{'b':b, 'users':users, 'users_as_table':users_as_table, 'transfers':transfers,'transfer_form':transfer_form},
		context_instance=RequestContext(request))

def boardgame_transfer(request):
	if request.method == 'POST':
		form = TransferForm(request.POST);
		if form.is_valid():
			cd = form.cleaned_data
			b = Boardgame.objects.get(id=cd['boardgame_id'])
			person_new = User.objects.get(username=cd['person_new_username'])
			transfer_type = cd['transfer_type']
			if transfer_type == 'o':
				person_old = b.owner
				b.owner = person_new
			elif transfer_type == 'p':
				person_old = b.patron
				b.patron = person_new
			else:
				person_old = b.holder
				b.holder = person_new
			b.save()

			t = Transfer(boardgame=b,person_old=person_old,person_new=person_new,type=transfer_type,desc=cd['desc'],changer=request.user)
			t.save()
	return HttpResponseRedirect('/boardgame/' + str(b.id) + '/')

def user_view(request,username):
	p = User.objects.get(username=username)

	#boardgames = p.boardgame_set.all()
	owner_of = Boardgame.objects.filter(owner=p)
	patron_of = Boardgame.objects.filter(patron=p)
	holder_of = Boardgame.objects.filter(holder=p)


	return render_to_response('user_view.html',
		{'vieweduser':p, 'owner_of':owner_of, 'patron_of':patron_of, 'holder_of':holder_of},
		context_instance=RequestContext(request))

def users_all(request):
	users = User.objects.all()
	return render_to_response('users_all.html',
		{'users_all':users},
		context_instance=RequestContext(request))

####################################################
## EVENTS
####################################################

def event_change_view(request):
	if request.method == 'POST':
		event_change_form = EventChangeForm(request.POST)
		if event_change_form.is_valid():
			cd = event_change_form.cleaned_data
			request.session['event']=Event.objects.get(id=cd['event_id'])
			return HttpResponseRedirect('/event/')
	if 'event' in request.session:
		event_change_form = EventChangeForm(initial={'event':request.session['event'].id})
	else:
		event_change_form = EventChangeForm()
	return render_to_response('event_change.html',
		{'event_change_form':event_change_form},
		context_instance=RequestContext(request))

def is_event_selected(request):
	return request.session['event'] == None or request.session['event'] == ''

def event_view(request):
	#if not 'event' in request.session:
	#	return HttpResponseRedirect('/event_change/')
	event_choises = Event.objects.all()
	if 'event' in request.session:
		event = request.session['event']
		bgs = EventBoardgame.objects.all().filter(event=event)
		lends = EventLendRecord.objects.all().filter(date_return=None).order_by('event_lender__number')
		lenders = EventLender.objects.filter(event=event).filter(number_datetime_return=None) #.sort('number')
	else:
		bgs = None
		lends = None
		lenders = None
	return render_to_response('event_view.html',
		{'bgs':bgs,'lends':lends,'lenders':lenders,'event_choices':event_choices},
		context_instance=RequestContext(request))
