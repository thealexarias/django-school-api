from django.db import models
from django.core import validators as v

# Create your models here.
class Student(models.Model):
    name = models.CharField(null=False, unique=False, default=None, validators=[])
    student_email = models.EmailField(null=False, unique=True, default=None, validators=[])
    personal_email = models.EmailField(null=True, unique=True, default=None)
    locker_number = models.IntegerField(null=False, unique=True, default=110, validators=[v.MinValueValidator(1), v.MaxValueValidator(200)])
    locker_combination = models.CharField(null=False, unique=False, default="12-12-12", validators=[])
    good_student = models.BooleanField(null=False, unique=False, default=True)

    def locker_reassignment(self, new_locker_number: int):
        self.locker_number = new_locker_number
        self.save()
    
    def student_status(self, new_student_status:bool):
        self.good_student = new_student_status
        self.save()

    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"