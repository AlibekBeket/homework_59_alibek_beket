from django.contrib import admin

from issue_tracker.models import *


# Register your models here.
class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "type_name")
    list_filter = ("id", "type_name")
    search_fields = ("id", "type_name")
    fields = ("type_name",)
    readonly_fields = ("id",)


admin.site.register(Type, TypeAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "status_name")
    list_filter = ("id", "status_name")
    search_fields = ("id", "status_name")
    fields = ("status_name",)
    readonly_fields = ("id",)


admin.site.register(Status, StatusAdmin)


class IssueAdmin(admin.ModelAdmin):
    list_display = ("id", "summary", "description", "status", "created_at", "updated_at")
    list_filter = ("id", "summary", "description", "status", "created_at", "updated_at")
    search_fields = ("id", "summary", "description", "status", "type")
    fields = ("summary", "description", "status", "type", "created_at", "updated_at")
    readonly_fields = ("id", "created_at", "updated_at")


admin.site.register(Issue, IssueAdmin)
