from django.db import models

# Create your models here.

class Department(models.Model):
    department_ID=models.AutoField(primary_key=True)
    department_name=models.CharField(max_length=30,verbose_name='department name')

    def __str__(self):
        return (str(self.department_ID))+" - "+(self.department_name)

    class Meta:
        verbose_name='Department'
        verbose_name_plural='Departments'