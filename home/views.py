from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
        person = {
          'name': 'john',
          'age': 0 ,
          'place':'Calicut'
        }
        return render(request,'index.html',person)

def about(request):
    return HttpResponse("About Page")
def booking(request):
    return HttpResponse("booking Page")
def doctors(request):
    return HttpResponse("doctors Page")
def contact(request):
    return HttpResponse("contact Page")