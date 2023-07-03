from django.contrib import admin
from main.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task','is_compeleted','updated')
    search_fields = ('task',)

admin.site.register(Task, TaskAdmin)
