from django.contrib import admin

# Register your models here.
from .models import Project, Task, Team, TaskActivity

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Team)
admin.site.register(TaskActivity)