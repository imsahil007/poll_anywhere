from django.contrib import admin

# Register your models here.

from .models import Poll, Choices
admin.site.register(Poll)
admin.site.register(Choices)