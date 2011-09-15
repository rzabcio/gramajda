# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TRANSFER_TYPES = (
	('o', 'właściciel'),
	('p', 'opiekun'),
	('h', 'posiadacz'),
)

#################################
## LIBRARY
#################################

class BoardgameMeta(models.Model):
	title = models.CharField(max_length=255, unique=True, verbose_name='Tytuł')
	bgg_link = models.URLField(max_length=255, verbose_name='Gra na BGG')
	min_players = models.IntegerField(blank=True)
	max_players = models.IntegerField(blank=True)
	min_time = models.IntegerField(blank=True)
	max_time = models.IntegerField(blank=True)
	min_age = models.IntegerField(blank=True)

	class Meta:
		verbose_name="Gra planszowa"
		verbose_name_plural="Gry planszowe"
	def __str__(self):
		return self.title
	def __unicode__(self):
		return self.title

class Boardgame(models.Model):
	meta = models.ForeignKey(BoardgameMeta)
	owner = models.ForeignKey(User, blank=True, related_name='owner')
	patron = models.ForeignKey(User, blank=True, related_name='patron')
	holder = models.ForeignKey(User, blank=True, related_name='holder')

	class Meta:
		verbose_name="Gra planszowa - egzemplarz"
		verbose_name_plural="Gry planszowe - egzemplarze"
	def __str__(self):
		return self.meta.title
	def __unicode__(self):
		return self.meta.title

class Transfer(models.Model):
	desc = models.CharField(max_length=255, verbose_name='Komentarz')
	boardgame = models.ForeignKey(Boardgame)
	person_new = models.ForeignKey(User, related_name='person_new')
	person_old = models.ForeignKey(User, related_name='person_old')
	type = models.CharField(max_length=1, choices=TRANSFER_TYPES)
	date = models.DateTimeField(auto_now_add=True)
	changer = models.ForeignKey(User, related_name='changer')

	class Meta:
		verbose_name="Transfer gry"
		verbose_name_plural="Transfery gier"
	def __str__(self):
		return self.date.__str__() + ' \"' + self.boardgame.title + '\" ' + self.person_old.username + " -> " + self.person_new.username + ' (' + self.changer.username + '\"' + self.desc + '\")'
	def __unicode(self):
		return self.date.__str__() + ' \"' + self.boardgame.title + '\" ' + self.person_old.username + " -> " + self.person_new.username + ' (' + self.changer.username + '\"' + self.desc + '\")'


###############################################
## EVENTS
###############################################

class Event(models.Model):
	title = models.CharField(max_length=255, unique=True, verbose_name="Nazwa imprezy")
	link = models.URLField(max_length=255, verify_exists=False, verbose_name="Link do imprezy")
	is_active = models.BooleanField(default=False)
	class Meta:
		verbose_name="Event - impreaza z wypożyczalnią"
                verbose_name_plural="Event - imprezy z wypożyczalnią"
	def __str__(self):
		return self.title
	def __unicode__(self):
		return self.title

ID_TYPES = (
	('id', 'dowód osobisty'),
	('leg', 'legitymacja uczniowska/studencka'),
	('mon', 'pieniądze'),
	('oth', 'inne'),
)

class EventLender(models.Model):
	event = models.ForeignKey(Event)
	name = models.CharField(max_length=100, unique=False)
	id_type = models.CharField(max_length=3, choices=ID_TYPES)
	number = models.IntegerField()
	number_datetime_get = models.DateTimeField(auto_now_add=True)
	number_datetime_return = models.DateTimeField(null=True,blank=True)
	class Meta:
		verbose_name="Event - osoba wypożyczająca"
                verbose_name_plural="Event - osoby wypożyczające"				
        def __str__(self):
		return '(' + str(self.number) + ') ' + self.name
        def __unicode__(self):
		return '(' + str(self.number) + ') ' + self.name

class EventBoardgame(models.Model):
	event = models.ForeignKey(Event)
	boardgame = models.ForeignKey(Boardgame)
	class Meta:
		verbose_name="Event - planszówka w wypożyczalni"
                verbose_name_plural="Event - planszówki w wypożyczalni"				
        def __str__(self):
		return self.boardgame.meta.title + ' (' + self.event.title + ')'
        def __unicode__(self):
		return self.boardgame.meta.title + ' (' + self.event.title + ')'

class EventLendRecord(models.Model):
	event = models.ForeignKey(Event)
	event_boardgame = models.ForeignKey(EventBoardgame)
	event_lender = models.ForeignKey(EventLender)
	date_get = models.DateTimeField(auto_now_add=True)
	date_return = models.DateTimeField(null=True,blank=True)

	class Meta:
                verbose_name="Event - zapis zypożyczenia"
                verbose_name_plural="Event - zapis wypożyczenia"
        def __str__(self):
		return '(' + str(self.event_lender.number) + ') - ' + self.event_boardgame.boardgame.meta.title
        def __unicode__(self):
		return '(' + str(self.event_lender.number) + ') - ' + self.event_boardgame.boardgame.meta.title


