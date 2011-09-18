# Create your views here.

import django
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core import serializers
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from grajteka.models import *

def boardgames_list(request):
	boardgames = Boardgame.objects.all().order_by("meta__title")
	data = serializers.serialize("json", boardgames, indent=2, use_natural_keys=True)
	return HttpResponse(data)
