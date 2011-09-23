# -*- coding: utf-8 -*-
from django.contrib import admin

#import pliku z modelami
from grajteka.models import *

class BoardgameAdmin(admin.ModelAdmin):
	list_display = ('meta','owner','holder','patron')

admin.site.register(GUser)
admin.site.register(Boardgame)
admin.site.register(BoardgameMeta)
admin.site.register(Transfer)
admin.site.register(Event)
admin.site.register(EventLender)
admin.site.register(EventBoardgame)
admin.site.register(EventLendRecord)
