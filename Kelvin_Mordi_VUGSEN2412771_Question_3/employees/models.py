from django.db import models

class Address(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"

class StaffBase(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        abstract = True

class Manager(StaffBase):
    department = models.CharField(max_length=100)
    has_company_card = models.BooleanField(default=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

class Intern(StaffBase):
    internship_end = models.DateField()
    has_company_card = models.BooleanField(default=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)