from django.http import HttpResponseRedirect
from django.shortcuts import redirect,render

def redirect_root(request):
    return redirect('/blog/')
