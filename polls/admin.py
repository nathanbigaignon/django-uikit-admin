from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('cool',               {'fields': ['question_text_one', 'question_text_two']}),
        ('Date information', {'fields': ['question_text_three', 'question_text_four', 'question_text_five', 'confirmation', 'second_confirmation', 'test_file']}),
    ]

admin.site.register(Question, QuestionAdmin)
