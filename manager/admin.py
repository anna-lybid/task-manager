from django.contrib import admin

from manager.models import TaskType, Position, Worker, Task

admin.site.register(TaskType)
admin.site.register(Position)
admin.site.register(Worker)
admin.site.register(Task)
