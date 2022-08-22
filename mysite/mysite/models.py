from django.db import models


class Employee(models.Model):
    empId = models.AutoField
    empName = models.CharField(max_length=100)
    empSalary = models.IntegerField(default=0)
    empDes = models.CharField(max_length=50)
    empDOJ = models.DateTimeField('Employee Joining Date')

    def __str__(self):
        return self.empName

    def toStrDate(self):
        return self.empDOJ.strftime('%d-%m-%Y %I:%M:%S %p')
