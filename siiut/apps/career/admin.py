from django.contrib import admin

from .models import Career, Subject, Level, Quarter

admin.site.register(Level)
admin.site.register(Quarter)
admin.site.register(Career)
admin.site.register(Subject)