from django.contrib import admin
from polls.models import Choice, Question

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	"""Segregate fields in the admin interface - works better than vanilla 'fields'"""
	fieldsets = [
	(None, {'fields': ['question_text']}),
	('Date information', {'fields':['pub_date'], 'classes':['collapse']}),] # Collapse class applies CSS for show/hide box
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']

	inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
