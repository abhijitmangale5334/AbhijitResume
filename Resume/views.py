from django.shortcuts import render


# Create your views here.
def homepage(requests):
    context={}
    return render(requests, 'index.html', context=context)
