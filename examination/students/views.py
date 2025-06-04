from django.http import HttpResponse  # type: ignore
from django.shortcuts import render  # type: ignore

# Create your views here.
from django.shortcuts import render  # type: ignore
from django.contrib.auth import authenticate, login  # type: ignore
from django.shortcuts import render, redirect  # type: ignore
from django.contrib import messages  # type: ignore
from django.contrib.auth.decorators import login_required  # type: ignore
def base(request):
    return render(request, 'students/base.html')
def login(request):
   return render(request, "students/login.html")
from django.shortcuts import render, redirect  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from django.contrib import messages  # type: ignore

def register(request):
    if request.method == 'POST':
        # Getting form data from POST request
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phoneno = request.POST.get('phoneno', '')  # Avoids KeyError
        # Check if all fields are filled
        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return render(request, 'students/register.html')

        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'students/register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'students/register.html')
        if StudentProfile.objects.filter(phoneno=phoneno).exists():
            messages.error(request, "Phone number already registered.")
            return render(request, 'students/register.html')
        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        StudentProfile.objects.create(user=user,phoneno=phoneno)

        # After successful registration, redirect to login page
        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')  # Redirect to login page after successful registration
    
    return render(request, 'students/register.html')
from django.urls import path, reverse # type: ignore
from django.shortcuts import render # type: ignore

from django.shortcuts import render # type: ignore
from exam.models import Exam

def dashboard(request):
    exams = Exam.objects.filter(user=request.user)  # Get exams for logged-in user
    return render(request, 'students/dashboard.html', {'exams': exams})

from django.shortcuts import render, get_object_or_404 # type: ignore
from .models import Exam  # Import Exam model

def results(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)  # Ensure exam exists
    return render(request, 'students/results.html', {'exam': exam})  # Pass exam to template


def logout(request):
    return render(request, 'students/logout.html')
from django.shortcuts import render  # type: ignore
from .models import ExamResult, StudentProfile  # Import the ExamResult model
from django.contrib.auth.decorators import login_required  # type: ignore

# In students/views.py

from django.shortcuts import render  # type: ignore
from .models import ExamResult
from django.contrib.auth.decorators import login_required  # type: ignore

# students/views.py
from django.shortcuts import render  # type: ignore
from .models import ExamResult
from django.contrib.auth.decorators import login_required  # type: ignore




from django.shortcuts import render, redirect  # type: ignore
from django.contrib.auth import authenticate, login  # type: ignore
from django.contrib.auth.decorators import login_required  # type: ignore
from django.contrib import messages  # type: ignore

def home(request):
    return render(request, "students/base.html")

from django.contrib.auth import authenticate, login  # type: ignore
from django.shortcuts import render, redirect  # type: ignore
from django.contrib.auth.forms import AuthenticationForm  # type: ignore
from django.views.decorators.csrf import csrf_exempt  # type: ignore

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(f"User {user.username} logged in.")  # Debugging line
            login(request, user)
            return redirect('dashboard')
        else:
          #  print(form.errors)  # Debugging line
            return render(request, 'students/login.html', {'form': form, 'error': 'Invalid credentials. Please try again.'})
    else:
        form = AuthenticationForm()
    
    return render(request, 'students/login.html', {'form': form})
def about(request):
    return render(request, "students/about.html")
from django.shortcuts import render, redirect  # type: ignore
from django.contrib import messages  # type: ignore
from .models import ContactMessage

def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, "Your message has been sent successfully!")
            return redirect("contactus")  # Redirect to clear the form

    return render(request, "students/contactus.html")


from django.shortcuts import render, get_object_or_404  # type: ignore
from .models import StudentProfile

def student_profile(request):
    # Check if profile exists
    student_profile, created = StudentProfile.objects.get_or_create(user=request.user)

    return render(request, "students/student_profile.html", {"student": student_profile})

def aboutus(request):
    return render(request, "students/aboutus.html")
from django.shortcuts import render, redirect  # type: ignore
from django.contrib import messages  # type: ignore
from .models import ContactMessage

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")  # Redirect to clear the form

    return render(request, "students/contact.html")


