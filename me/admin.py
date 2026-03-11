from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username', 'rollno', 'section')
    list_filter = ('section',)
    search_fields = ('username', 'rollno')
