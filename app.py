from flask import (
    Flask,
    render_template as render
    )
app = Flask(__name__)

@app.route('/')
def home():
    context = {
        'Title': 'Austen C. Myers',
        'Subtitle': 'Professional Profile',
        "description": "Have a look around.",
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
    return render('base.html', **context)

@app.route('/bio')
def bio():
    context = {
        'Title': 'Austen C. Myers',
        'Subtitle': 'Professional Profile',
        "description": "Just a little about me.",
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
            'url': 'assets/documents/resume.pdf'
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
    bio = {
        'Title': 'bio',
        'entries': [
            {
                'Title': 'geography'
            }
            ]
    }
    return render('base.html', **context, section=bio)

@app.route('/employment')
def employment():
    context = {
        'Title': 'Austen C. Myers',
        'Subtitle': 'Professional Profile',
        "description": "Where I've worked.",
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
            'url': 'assets/documents/resume.pdf'
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
    employment = {
        'Title': 'employment',
        'entries': [
            {
                'Title': 'national guard'
            }
            ]
    }
    return render('base.html', **context, section=employment)

@app.route('/education')
def education():
    context = {
        'Title': 'Austen C. Myers',
        'Subtitle': 'Professional Profile',
        "description": "What I've been taught.",
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
            'url': 'assets/documents/resume.pdf'
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
    education = {
        'Title': 'education',
        'entries': [
            {
                'Title': 'training'
            }
            ]
    }
    return render('base.html', **context, section=education)

@app.route('/skills')
def skills():
    context = {
        'Title': 'Austen C. Myers',
        'Subtitle': 'Professional Profile',
        "description": "Things I've picked up.",
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
            'url': 'assets/documents/resume.pdf'
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
    skills = {
        'Title': 'skills',
        'entries': [
            {
                'Title': 'programming languages'
            }
            ]
    }
    return render('base.html', **context, section=skills)
