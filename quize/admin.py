from django.contrib import admin
from quize.models import Question, Quize, Tag, UserQuize, QuizeAnswers

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

class QuizeAnswerAdmin(admin.ModelAdmin):
    list_display = ('quize', "question", "ans", "correct")

class UserQuizeAdmin(admin.ModelAdmin):
    list_display = ("user", "quize")

admin.site.register(Quize, QuizeAdmin)
admin.site.register(Tag)
admin.site.register(UserQuize, UserQuizeAdmin)
admin.site.register(QuizeAnswers, QuizeAnswerAdmin)