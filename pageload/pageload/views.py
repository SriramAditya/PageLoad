from django.shortcuts import render
from .forms import LoginForm
import json

with open('pageload.json') as d:
    for item in d:
        print("item:",item)
        #data = json.load(d)
# Create your views here.
def home_page(request):
    return render(request, 'index.html')

def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request, 'index.html', {})
        else:
            return render(request, 'login.html', {'form': form})
    if request.method == 'GET':
        form = LoginForm(request.GET)
        if form.is_valid():
            return render('index.html', {})
        else:
            return render(request, 'login.html', {'form': form})

def pageload(request):
    f = open("pageload.json")
    lines = f.readlines()
    data = []
    for v in lines:
        d = json.loads(v)
        data.append(d)
    return render(request, 'pageload.html',{"data":data})
