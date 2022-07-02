from django.contrib import admin
from .models import Color, Type, Question, Choice

admin.site.register(Color)
admin.site.register(Type)
admin.site.register(Question)
admin.site.register(Choice)