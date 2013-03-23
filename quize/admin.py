from django.contrib import admin
from quize.models import Question, Quize

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'date_added')
    search_fields = ('text',)
    list_filter = ('date_added',)
    date_hierarchy = 'date_added'
    ordering = ('-date_added',)
    fields = ('user', 'text', 'opt1', 'opt2', 'opt3', 'opt4', 'ans')
    
admin.site.register(Question, QuestionAdmin)


class QuizeAdmin(admin.ModelAdmin):
    filter_horizontal = ('questions',)

admin.site.register(Quize, QuizeAdmin)
