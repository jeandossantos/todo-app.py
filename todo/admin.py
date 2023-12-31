from django.contrib import admin
from .models import Todo
# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ['created_at',
                    'title',
                    'description',
                    'priority',
                    'deadline',
                    'done']


admin.site.register(Todo, TodoAdmin)
