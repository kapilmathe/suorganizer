from django.shortcuts import render

# Create your views here.


def about(request):
    template = 'staticpage/about.html'
    return render(request,template)

def contact(request):
    template = 'staticpage/contact.html'
    return render(request,template)
