from django.contrib import admin
from .models import (
    Project,
    Employee,
    Team,
    Version,
    Task
)


class EmployeeAdminInline(admin.StackedInline):
    model = Employee
    fields = ("name",)
    extra = 2


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = ("id", "name", "status", "manager")
    list_filter = ("name", "status")


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = (
        "id", "name", "birthdate", "position", "salary", "team", "task_number"
    )
    list_filter = ("name", "position", "salary", "team")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = ("id", "name", "description", "project",
                    "version_created", "version_completed")
    list_filter = ("name", "project", "version_created", "version_completed")


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = ("id", "name", "description", "release_datetime", "project")
    list_filter = ("name", "project")


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = ("id", "name", "description", "profile")
    list_filter = ("name", "profile")
