from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):

    name = "YOUNG LEARNERS"
    Coursedetails = {
        "Course_name" :{
            "name":"Python"
            "fees""Two"
            "duration""Two Months",
            "branch":"All branch",
            "faculty name":"k.Raman sir",
            "batch timing":"morning batch",
        
    }
            
       }
    
    context = { "display_name":name, "Course_details":Coursedetails }
    return render(request,"home.html",context )