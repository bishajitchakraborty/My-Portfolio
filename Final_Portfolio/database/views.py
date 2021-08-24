from django.shortcuts import render
from .models import Profile
from .models import Professions,About,Educations,Contact,Services,Skills,Experiernces

# Create your views here.
def home(request):
    profile=Profile.objects.all()
    professions=Professions.objects.all()
    about=About.objects.all()
    education=Educations.objects.all()
    contact=Contact.objects.all()
    services=Services.objects.all()
    skills=Skills.objects.all()
    experiernces=Experiernces.objects.all()
    return render(request, 'database/home.html',{'profile':profile,'professions':professions,'about':about,'education':education,
                   'contact':contact,'services':services,'skills':skills,'experiernces':experiernces})
