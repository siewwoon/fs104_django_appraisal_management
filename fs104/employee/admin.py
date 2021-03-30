from django.contrib import admin
from .models import Employee
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_ID','first_name','last_name','email','contact','address','manager_ID','department_ID','hire_date','is_active')
