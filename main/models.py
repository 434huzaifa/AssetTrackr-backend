from django.db import models
from django.db.models import (
    CharField,
    EmailField,
    UUIDField,
    ForeignKey,
    DateTimeField,
    BooleanField
)
import uuid
from django.utils import timezone

# Create your models here.
class Company(models.Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    title = CharField(max_length=150, null=True, blank=True)
    email = EmailField(null=True, blank=True, unique=True)
    password = CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class Employee(models.Model):
    company = ForeignKey(Company, on_delete=models.CASCADE)
    name = CharField(max_length=150, null=True, blank=True)
    delegate = CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


CONDITION_CHOICES = [
    ("Excellent", "Excellent"),
    ("Good", "Good"),
    ("Fair", "Fair"),
    ("Poor", "Poor"),
]


class Device(models.Model):
    company = ForeignKey(Company, on_delete=models.CASCADE)
    condition = CharField(max_length=20, choices=CONDITION_CHOICES)
    name = CharField(max_length=150, null=True, blank=True)
    def __str__(self):
        return f'{self.name}'

class Checkout(models.Model):
    employee = ForeignKey(Employee, on_delete=models.CASCADE)
    device = ForeignKey(Device, on_delete=models.CASCADE)
    checkout_date = DateTimeField(default=timezone.now)
    return_date = DateTimeField(null=True, blank=True)
    checkout_condition = CharField(max_length=20, choices=CONDITION_CHOICES)
    return_condition = CharField(max_length=20, choices=CONDITION_CHOICES, null=True, blank=True)
    isReturn = BooleanField(default=False)
    
    def __str__(self):
        return f"{self.employee} - {self.device} - {self.checkout_date}"