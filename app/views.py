from django.shortcuts import render
from .models.utility import Link, Page

context = {
        'links': Link.objects.all(),
        'pages': Page.objects.all(),
}

def home(Request):
    context.update({
        'page': Page.objects.get(label='home')
    })
    return render(Request, 'home.html', context)

def bio(Request):
    from .models.bio import Story
    context.update({
        'page': Page.objects.get(label='bio'),
        'stories': Story.objects.all()
    })
    return render(Request, 'bio.html', context)

def work(Request):
    from .models.work import Employer
    context.update({
        'page': Page.objects.get(label='employment'),
        'employers': Employer.objects.all()
    })
    return render(Request, 'work.html', context)

def edu(Request):
    from .models.edu import Provider
    context.update({
        'page': Page.objects.get(label='education'),
        'providers': Provider.objects.all()
    })
    return render(Request, 'edu.html', context)

def skills(Request):
    from .models.skills import Skill
    context.update({
        'page': Page.objects.get(label='skills'),
        'skills': Skill.objects.all(),
    })
    return render(Request, 'skills.html', context)