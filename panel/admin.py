from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Plan, Userprofile


# Register your models here.
class ImportExport(ImportExportModelAdmin, admin.ModelAdmin):
    pass


@admin.register(Plan)
class PLAN(ImportExport):
    list_display = (
        'plan_name',
        'description',
        'Duration',
        'cost',
    )


@admin.register(Userprofile)
class USER(ImportExport):
    list_display = (
        'user',
        'first_name',
        'last_name',
        'address',
        'email',
        'profile_image',
        'current_plan',
        'phone_number',
    )
