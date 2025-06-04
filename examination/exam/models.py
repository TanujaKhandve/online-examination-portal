from django.db import models # type: ignore

# Create your models here.
from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore

# Model for an Exam
class Exam(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    total_marks = models.IntegerField()

    def __str__(self):
        return self.name

# Model for a Question in an Exam
class Question(models.Model):
    exam = models.ForeignKey(Exam, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    marks = models.IntegerField()

    def __str__(self):
        return self.text

# Model for Options in a Question
class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

# Model for storing Results
class Result(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    total_marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.username} - {self.exam.name}"
class Answer(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)  # The student who answered the question
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)  # The exam the question belongs to
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # The question being answered
    option = models.ForeignKey(Option, on_delete=models.CASCADE)  # The option selected by the student
    is_correct = models.BooleanField(default=False)  # Whether the selected answer is correct or not
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp of when the answer was submitted

    def __str__(self):
        return f"Answer by {self.student.username} for {self.question.text}"