from django.contrib import admin

from .models import *


@admin.register(Audio)
class FilterAudio(admin.ModelAdmin):
    list_display = (
        "id",
        "text_up",
        "text_down",
        "seekbar",
        "src",
        "file",
    )



@admin.register(GetCourseUser)
class FilterGetCourseUser(admin.ModelAdmin):
    list_display = (
        "id",
        "accountUserId",
        "get_audios",
    )
