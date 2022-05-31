from multiprocessing import context
from django import forms
from django.shortcuts import render
from .models import Entry

# Create your views here.
def index(request):

    context = {
        "inputFieldOne": Entry.inputFieldOne,
        "inputFiledTwo": Entry.inputFieldTwo,
    }

    return render(request, 'login/login.html', context=context)

def submit(request):
    return render(request, 'table/table.html')