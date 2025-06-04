from django.db import models # type: ignore

# Create your models here.
# In exams/models.py
from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore
# Correct import of Exam model from the exam app
'''from exam.models import Exam  # Import from exam app

# Your other model code for ExamResult or any other models
class ExamResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming User is your user model
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)  # Reference to Exam model
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.exam.name} - {self.score}"
'''
# students/models.py
from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore
from exam.models import Exam  # Importing the Exam model from the 'exam' app

class ExamResult(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'result'  # Points to the existing table in the database

from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phoneno = models.CharField(max_length=15, unique=True, default="0000000000")  # Default value added

    # Add more fields if needed (e.g., phone, age, etc.)

    def __str__(self):
        return self.user.username

from django.db import models # type: ignore

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
