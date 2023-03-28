from django.contrib import admin

# Register your models here.
from .models import *

class CompanyAdmin(admin.ModelAdmin):
    resource_class = Company
    list_display = (
        'name',
        'uuid',
        'address',
        'member_count',
        'floor_count',
        'tax_code',
        'get_child_company',
        'created_at',
        'updated_at',
    )
    search_fields = ('name',
        'uuid',
     )
admin.site.register(Company, CompanyAdmin)

class UnitAdmin(admin.ModelAdmin):
    pass
admin.site.register(Unit, UnitAdmin)

class SalaryPeriodDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(SalaryPeriodDetails, SalaryPeriodDetailsAdmin)

class SalaryTemplateAdmin(admin.ModelAdmin):
    resource_class = SalaryTemplate
    list_display = (
        'code',
        'name',
        'salary',
        'salary_kpi',
        'company',
    )
admin.site.register(SalaryTemplate, SalaryTemplateAdmin)

class StaffAdmin(admin.ModelAdmin):
    resource_class = Staff
    list_display = (
        'name',
        # 'image',
        'uuid',
        'address',
        'get_all_work_day_by_period',
        'get_all_salary_work_day_by_period',
        'get_all_salary_by_period',
        'tax_code',
        'title',
        'created_at',
        'updated_at',
    )
    search_fields = ('name',
        # 'image',
        'uuid',
     )
admin.site.register(Staff, StaffAdmin)


class TitleAdmin(admin.ModelAdmin):
    pass
admin.site.register(Title, TitleAdmin)

class WorkDayAdmin(admin.ModelAdmin):
    pass
admin.site.register(WorkDay, WorkDayAdmin)

class SalaryPaperAdmin(admin.ModelAdmin):
    resource_class = SalaryPaper
    list_display = (
        'name',
        'uuid',
        # 'export_salary_paper_by_period',
        'created_at',
        'updated_at',
    )
    search_fields = ('name',
        'uuid',
     )
    pass
admin.site.register(SalaryPaper, SalaryPaperAdmin)


