from django.contrib import admin
from .models import Appraisal, manager
# Register your models here

@admin.register(Appraisal)
class AppraisalAdmin(admin.ModelAdmin):
    list_display = ('appraisal_ID','objective','review_year','department_ID','employee_ID','rating')

@admin.register(manager)
class managerAdmin(admin.ModelAdmin):
    list_display = ('manager_ID','manager_name')