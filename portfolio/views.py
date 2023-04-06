from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Project

def portfolio_base(request):
    return render(request, 'portfolio/base.html', {})

def portfolio_home(request):
    context = {
        'name': 'Janak Datta Dandamudi',
        'photo_url': 'https://example.com/photo.jpg',
        'email': 'jd783@njit.edu',
        'github_url': 'https://github.com/DattaDandamudi',
    }
    return render(request, 'portfolio/home.html', context)

def portfolio_portfolio(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'portfolio/portfolio.html', context)

def portfolio_about(request):
    context = {
        'bio': ' I am a passionate and dedicated graduate student pursuing a Masters degree in Cybersecurity at the New Jersey Institute of Technology. With a strong background in computer science and a keen interest in data privacy and online security, I am committed to making the digital world a safer place',
    }
    return render(request, 'portfolio/about.html', context)

def portfolio_resume(request):
    return render(request, 'portfolio/resume.html',{})
