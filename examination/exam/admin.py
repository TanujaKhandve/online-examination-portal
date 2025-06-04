from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Exam, Question, Option, Result

class OptionInline(admin.TabularInline):
    model = Option
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

admin.site.register(Exam)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Result)
