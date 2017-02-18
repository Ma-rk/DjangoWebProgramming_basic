from django.contrib import admin
from polls.models import Question, Answer

admin.site.register(Question)
admin.site.register(Answer)
