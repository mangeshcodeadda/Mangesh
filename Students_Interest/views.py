from multiprocessing import context 
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    name= "altaf"
    StudentsInterest = {
        "course_interest" :{
            "name":"Python"
        }
    }
    context = {"dispaly_name":name,"Students_Interest":StudentsInterest}
    return render(request,"home.html",context)