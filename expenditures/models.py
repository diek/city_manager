from django.db import models


class Salary(models.Model):
    name = models.CharField(max_length=200)
    position_title = models.CharField(max_length=200)
    department = models.CharField(max_length=200, db_index=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
