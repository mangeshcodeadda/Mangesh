from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    name="nitin"
    CourseSearch = {
        "Course_name" :{
            "name":"python",
            "name":"IoT",
            "name":"Soft Skill",
            "name":"AI"

        }
    }
    context = {"display_name":name, "Course_Search":CourseSearch}
    return render(request,"home.html",context)