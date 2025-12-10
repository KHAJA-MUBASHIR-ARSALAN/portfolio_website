from django.shortcuts import render,redirect
from .models import Skill,About,TimelineEntry,Profile,Internship,Project,Certificate
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse,Http404
from django.conf import settings
import os

# Create your views here.
# def home(request):
#     return render(request, "portfolio_app/index.html")


# def portfolio(request):
#     skills = Skill.objects.all()
#     about = About.objects.first()
#     return render(request, "index.html", {"skills": skills,"about":about})



def portfolio(request):
    skills = Skill.objects.all()
    about = About.objects.first()
    education = TimelineEntry.objects.filter(entry_type="education")
    experience = TimelineEntry.objects.filter(entry_type="experience")
    profile = Profile.objects.first()
    internships = Internship.objects.all()
    projects = Project.objects.all()
    certificates = Certificate.objects.all()

    context = {
        "skills": skills,
        "about": about,
        "education": education,
        "experience": experience,
        "profile": profile,
        "internships": internships,
        "projects": projects,
        "certificates" : certificates,
    }
    return render(request, "portfolio_app/index.html", context)



def google_verification(request):
    file_path = os.path.join(settings.BASE_DIR, 'google906ecfcb3556e71a.html')
    if not os.path.exists(file_path):
        raise Http404("Verification file not found.")
    with open(file_path, 'r') as file:
        return HttpResponse(file.read(), content_type="text/html")
