from django.db import models
from department.models import Department
# Create your models here.

class Appraisal(models.Model):
    appraisal_ID = models.AutoField(primary_key=True)
    objective = models.CharField(max_length=40,verbose_name='objective')
    review_year = models.CharField(max_length=4,verbose_name='review year')
    department_ID = models.ForeignKey(Department,on_delete=models.CASCADE)
    employee_ID = models.ForeignKey("employee.Employee",on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return (str(self.appraisal_ID))+" - "+(self.review_year)

    class Meta:
        verbose_name = 'Appraisal'
        verbose_name_plural = 'Appraisals'

class manager(models.Model):
    manager_ID = models.AutoField(primary_key=True)
    manager_name=models.CharField(max_length=50,verbose_name='manager name')

    def __str__(self):
        return (str(self.manager_ID))+" - "+self.manager_name

    class Meta:
        verbose_name='manager'
        verbose_name_plural='managers'