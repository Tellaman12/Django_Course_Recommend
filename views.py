from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course

@login_required
def home(request):
    """Renders the home page for authenticated users."""
    return render(request, 'home.html')

@login_required
def preferences(request):
    """Renders the user preferences page."""
    return render(request, 'preferences.html')

@login_required
def courses(request):
    """Displays all available courses."""
    all_courses = Course.objects.all()
    return render(request, 'courses.html', {'all_courses': all_courses})

@login_required
def enroll_course(request, course_id):
    """
    Renders the courses page, potentially with past winners content.
    """
    # Render the courses page with content for past winners
    return render(request, 'courses.html')

