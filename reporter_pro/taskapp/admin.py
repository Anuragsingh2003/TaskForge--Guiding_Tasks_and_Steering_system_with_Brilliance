from django.contrib import admin

# Register your models here.

from .models import Tasks,Leave_apply

admin.site.register(Tasks)
admin.site.register(Leave_apply)
