from django.db import models
from django.db.models.deletion import SET_NULL

# Create your models here.

SPESIFICATION = [
    ('WEB DEVELOPMENT', 'WEB DEVELOPMENT'),
    ('MOBILE APP DEVELOPMENT', 'MOBILE APP DEVELOPMENT'),
    ('DESKTOP DEVELOPMENT', 'DESKTOP DEVELOPMENT'),
]


DEVELOPER_TECH = [
    ("FRONTEND", "FRONTEND"),
    ("BACKEND", "BACKEND"),
    ("WEB FULLSTACK", "WEB FULLSTACK"),
    ("ANDROID", "ANDROID"),
    ("IOS", "IOS"),
    ("FLUTTER", "FLUTTER"),
    ("REACT NATIVE", "REACT NATIVE"),
    ("DESKTOP APPS", "DESKTOP APPS"),
]

LEVEL = [
    ("JUNIOR", "JUNIOR"),
    ("MIDDLE", "MIDDLE"), 
    ("SENIOR", "SENIOR"),
]


PAYMENT_STATUS = [
    ("PAID", "PAID"),
    ("UNPAID", "UNPAID"), 
]


LESSON_TIME = [
    ("10:00 - 12:00", "10:00 - 12:00"),
    ("14:00 - 16:00", "14:00 - 16:00"),
    ("17:00 - 19:00", "17:00 - 19:00"), 
]

LESSON_STATUS = [
    ("PLANNED", "PLANNED"),
    ("COMPLETED", "COMPLETED"), 
    ("CANCELED", "CANCELED"), 
]

class Mentor(models.Model):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    spesification = models.CharField(max_length=23, choices=SPESIFICATION, default="WEB DEVELOPMENT")
    developer_tech = models.CharField(max_length=14, choices=DEVELOPER_TECH, default="FRONTEND")
    level = models.CharField(max_length=7, choices=LEVEL, default="JUNIOR")

    def __str__(self):
        return self.full_name


class Group(models.Model):
    name = models.CharField(max_length=40)
    spesification = models.CharField(max_length=23, choices=SPESIFICATION, default="WEB DEVELOPMENT")
    developer_tech = models.CharField(max_length=14, choices=DEVELOPER_TECH, default="FRONTEND")
    mentor = models.ForeignKey(Mentor, on_delete=SET_NULL, blank=True, null=True)
    start_date = models.DateField()
    finish_date = models.DateField()

    def __str__(self):
        return self.name



class Student(models.Model):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone = models.PositiveIntegerField()
    email = models.EmailField()
    group = models.ForeignKey(Group, on_delete=SET_NULL, blank=True, null=True)
    payment_status = models.CharField(max_length=7, choices=PAYMENT_STATUS, default="UNPAID")

    def __str__(self):
        return self.full_name



class Lesson(models.Model):
    lesson_date = models.DateField()
    lesson_time = models.CharField(max_length=15, choices=LESSON_TIME, default="10:00 - 12:00")
    group = models.ForeignKey(Group, on_delete=SET_NULL, blank=True, null=True)
    mentor = models.ForeignKey(Mentor, on_delete=SET_NULL, blank=True, null=True)
    lesson_status = models.CharField(max_length=10, choices=LESSON_STATUS, default="PLANNED")


