from django.shortcuts import render

# Create your views here.

from home.models import CustomText, HomePage


def home(request):
    packages = [
	{'name':'stripe', 'url': 'http://pypi.python.org/pypi/stripe/1.77.1'},
	{'name':'dwolla', 'url': 'https://rubygems.org/gems/dwolla'},
	{'name':'django-mongodb-engine', 'url': 'http://pypi.python.org/pypi/django-mongodb-engine/0.6.0'},
	{'name':'SpeechRecognition', 'url': 'http://pypi.python.org/pypi/SpeechRecognition/3.8.1'},
	{'name':'djangorestframework', 'url': 'http://pypi.python.org/pypi/djangorestframework/3.7.7'},
	{'name':'django-bootstrap4', 'url': 'http://pypi.python.org/pypi/django-bootstrap4/0.0.5'},
	{'name':'django-allauth', 'url': 'http://pypi.python.org/pypi/django-allauth/0.34.0'},
    ]
    context = {
        'customtext': CustomText.objects.first(),
        'homepage': HomePage.objects.first(),
        'packages': packages
    }
    return render(request, 'home/index.html', context)
