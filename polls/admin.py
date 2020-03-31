from django.contrib import admin

from .models import Choice ,Question

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    list_display =('question_text','pub_date','was_published_recently')

    # fields = ['question_text','pub_date']
    fieldsets = [
        ( None, {"fields": ['question_text']}),
        ('Date information', {'fields': ['pub_date','expires_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_filter = ['pub_date']
    search_fields = ['question_text']


# Register your models here.
admin.site.register(Question, QuestionAdmin)