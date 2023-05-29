from django.utils import timezone

from django.db import models


# Company Model
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    location = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=(('IT', 'IT'), ('Non IT', 'Non IT')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "name= " + self.name + ". Company id=" + str(self.company_id)


# Employee Model
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    position = models.CharField(max_length=50, choices=(
        ('manager', 'manager'),
        ('Software Developer', 'sd'),
        ('Project Leader', 'pl')
    ))

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return "name= " + self.name + ". Company id=" + str(self.company.company_id)

# Employee-Products Model
class EmployeeProducts(models.Model):
    CONDITION = (('New', 'New'), ('Old', 'Old'), ('Bad', 'Bad'), ('Damaged', 'Damaged'))
    products = (('Phones', 'Phones'), ('Tablets', 'Tablets'), ('Laptops', 'Laptops'), ('Others', 'others'))

    Employee_name = models.ForeignKey(Employee, on_delete=models.CASCADE, default=1)
    Employee_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Product_name = models.CharField(choices=products, max_length=200, default='phone')
    Condition = models.CharField(choices=CONDITION, max_length=100, default='New')
    information = models.TextField()
    Given_Date = models.DateTimeField(default=timezone.now)
    Taken_Date = models.DateTimeField(default=timezone.now)
