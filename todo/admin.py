from django.contrib import admin

# Register your models here.
from .models import Topic, TodoItem

admin.site.register(Topic)
admin.site.register(TodoItem)