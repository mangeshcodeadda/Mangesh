from django.shortcuts import render,HttpResponse,redirect
from .forms import Mentord
from .models import mentord
# Create your views here.
# def home(request):
#     return 
def details(request):
    form=Mentord(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('detailsall')
    return render(request,'form.html',{'form':form})

def detailsall(request):
    data=mentord.objects.all()
    return render(request,'detailsall.html',{'data':data})

def detailsdelete(request):
    if request.method=="POST":
        ID=request.POST.get("Id")
        d=mentord.objects.filter(id=ID)
        d.delete()
        return redirect('detailsall')
    return render(request,'delete.html')

def update(request):
    if request.method=="POST":
        uID=request.POST.get('UID')
        Name=request.POST.get("name")
        Subject=request.POST.get("subject")
        Experiance=request.POST.get("experiance")
        Contact=request.POST.get("contact")
        Email=request.POST.get("email")
        a=mentord.objects.filter(id=uID).update(name=Name,subject=Subject,experiance=Experiance,contact=Contact,email=Email)
        return redirect('detailsall')
    return render(request,'update.html')
