from django.contrib import admin

# Register your models here.
from .models import Participant

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Participant)