# exams/views.py
from django.shortcuts import render # type: ignore
from .import views 


from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from .models import Exam, Question, Option, Result

# View for listing available exams
def exam_list(request):
    exams = Exam.objects.all()  # Get all exams
    return render(request, 'exam/exam_list.html', {'exams': exams})

# View for starting an exam
def exam_start(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    questions = exam.questions.all()  # Get all questions for the exam

    if request.method == 'POST':
        marks_obtained = 0
        for question in questions:
            selected_option_id = request.POST.get(f'q{question.id}')
            if selected_option_id:
                selected_option = Option.objects.get(id=selected_option_id)
                if selected_option.is_correct:
                    marks_obtained += question.marks

        # Save the result
        result = Result.objects.create(
            student=request.user,  # Assuming user is authenticated
            exam=exam,
            marks_obtained=marks_obtained,
            total_marks=exam.total_marks
        )
        return redirect('exam/exam_result', exam_id=exam.id)

    return render(request, 'exam/exam_start.html', {'exam': exam, 'questions': questions})

# View for showing exam result
from django.shortcuts import render # type: ignore
from .models import Exam, Question, Option, Answer

from django.shortcuts import render, get_object_or_404 # type: ignore
from .models import Exam

def exam_result(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    student = request.user

    # Get the student's result for this exam
    result = Result.objects.filter(student=student, exam=exam).first()

    if result:
        return render(request, 'exam/exam_result.html', {'result': result, 'exam': exam})
    else:
        # If the result doesn't exist, handle it gracefully (e.g., display an error message)
        return render(request, 'exam/exam_result.html', {'exam': exam, 'result': None})

from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from django.contrib.auth.models import User # type: ignore
from .models import Exam, Result, Option

from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from django.contrib.auth.models import User # type: ignore
from .models import Exam, Result, Option

def submit_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    student = request.user  # Assuming the user is logged in

    if request.method == 'POST':
        total_marks = 0
        marks_obtained = 0

        print("DEBUG: Exam submission started")  # Step 1: Print when submission starts
        print("DEBUG: Received POST Data ->", request.POST)  # Step 2: Check what data is received

        # Iterate through all the questions in the exam
        for question in exam.questions.all():
            # Get the selected option id from the form
            selected_option_id = request.POST.get(f'question_{question.id}')
            
            print(f"DEBUG: Processing Question: {question.text}, Selected Option ID: {selected_option_id}")  # Step 3: Check question & selected option

            if selected_option_id:
                # Get the selected option
                selected_option = get_object_or_404(Option, id=selected_option_id, question=question)
                
                print(f"DEBUG: Selected Option Text: {selected_option.text}, Is Correct: {selected_option.is_correct}")  # Step 4: Check if correct

                # If the option is correct, add the marks
                if selected_option.is_correct:
                    marks_obtained += question.marks
                    print(f"DEBUG: Correct Answer! Updated Marks: {marks_obtained}")  # Step 5: Print updated marks

            total_marks += question.marks

        print(f"DEBUG: Final Marks -> Obtained: {marks_obtained}, Total: {total_marks}")  # Step 6: Final marks before saving

        # Ensure marks_obtained is not None or 0 if no correct answer
        marks_obtained = marks_obtained if marks_obtained > 0 else 0

        # Check if the result already exists for this student and exam
        existing_result = Result.objects.filter(student=student, exam=exam).first()

        if not existing_result:  # If no existing result, create one
            result = Result.objects.create(
                student=student,
                exam=exam,
                marks_obtained=marks_obtained,
                total_marks=total_marks
            )
            print("DEBUG: New result created successfully")
        else:
            # If result exists, update the existing result
            existing_result.marks_obtained = marks_obtained
            existing_result.total_marks = total_marks
            existing_result.save()  # Save the updated result
            print("DEBUG: Existing result updated successfully")

        # Redirect to the result page (or any page where you want to show the result)
        return redirect('exam_result', exam_id=exam.id)

    # If it's a GET request, return the exam start page (if necessary)
    return render(request, 'exam/exam_start.html', {'exam': exam})
from django.shortcuts import render # type: ignore
from django.urls import reverse # type: ignore
from .models import Result

from django.shortcuts import render # type: ignore
from django.urls import reverse # type: ignore
from .models import Result

from django.urls import reverse # type: ignore

def dashboard(request):
    # Get all results for the logged-in student
    results = Result.objects.filter(student=request.user)

    if results.exists():  # Check if the student has any results
        results_urls = {result.exam.id: reverse('exam_result', args=[result.exam.id]) for result in results}
    else:
        results_urls = None  # No results available

    return render(request, 'students/dashboard.html', {'results_urls': results_urls})

