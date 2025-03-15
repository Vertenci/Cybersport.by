from django.contrib import admin
from .models import Teams


class TeamsAdmin(admin.ModelAdmin):
    filter_horizontal = ('players',)


admin.site.register(Teams)
