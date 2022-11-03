from django.contrib import admin

from base.models import TodoApp

# Register your models here.

class TodoAppAdmin(admin.ModelAdmin):
    list_display=(
        'title',
        'description',
        'created',
        'is_reading',
    )


admin.site.register(TodoApp, TodoAppAdmin)

