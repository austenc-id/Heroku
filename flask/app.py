from flask import (
    Flask,
    render_template as render
    )
app = Flask(__name__)

context = {
        'Title': 'Austen C. Myers',
        'Subtitle': 'Professional Profile',
        'links': [
            {
            'label': 'Github',
            'url': 'https://github.com/austenc-id'
            },
            {
            'label': 'LinkedIn',
            'url': 'https://www.linkedin.com/in/austenc-id/'
            },
            {
            'label': 'Resume',
            'url': 'static/downloads/resume.pdf'
            }
        ],
        'sections': [
            {
                'label': 'bio'
            },
            {
                'label': 'employment'
            },
            {
                'label': 'education'
            },
            {
                'label': 'skills'
            },
        ]
    }

@app.route('/')
def home():
    home = {
        'Title': 'home',
        "description": "Have a look around.",

    }
    return render('page.html', **context, section=home)

@app.route('/bio')
def bio():
    bio = {
        'Title': 'bio',
        "description": "Just a little about me.",
        'entries': [
            'ambitions',
            'interests',
            'locations',
            'family'
            ]
    }
    return render('page.html', **context, section=bio)

@app.route('/employment')
def employment():
    employment = {
        'Title': 'employment',
        "description": "Where I've worked.",
        'entries': [
            'national guard',
            'conduent',
            'sun valley resort',
            'kimobean'
            ]
    }
    return render('page.html', **context, section=employment)

@app.route('/education')
def education():
    education = {
        'Title': 'education',
        "description": "What I've been taught.",
        'entries': [
            'training',
            'academic',
            'independent'
            ]
    }
    return render('page.html', **context, section=education)

@app.route('/skills')
def skills():
    skills = {
        'Title': 'skills',
        "description": "Things I've picked up.",
        'entries': [
            'programming',
            'technology',
            'medical',
            'food service',
            ]
    }
    return render('page.html', **context, section=skills)
