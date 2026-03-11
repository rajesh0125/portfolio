from django.db import models
from django.db import models

class Student(models.Model):
    # Sections available - you can customize these
    SECTION_CHOICES = [
        ('A', 'Section A'),
        ('B', 'Section B'),
        ('C', 'Section C'),
        ('D', 'Section D'),
    ]
    
    username = models.CharField(max_length=100, unique=True)
    rollno = models.IntegerField(unique=True)
    section = models.CharField(max_length=1, choices=SECTION_CHOICES)
    
    def __str__(self):
        return f"{self.username} (Roll: {self.rollno}, Section: {self.section})"