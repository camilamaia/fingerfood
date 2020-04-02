from django.contrib import admin
from go_practice.models import Exercise


class ExerciseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Exercise, ExerciseAdmin)
