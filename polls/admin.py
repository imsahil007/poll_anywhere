from django.contrib import admin

# Register your models here.

from .models import Poll, PollChoices
admin.site.register(Poll)
admin.site.register(PollChoices)