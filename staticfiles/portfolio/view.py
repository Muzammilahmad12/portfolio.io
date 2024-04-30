from django.shortcuts import render
from django.http import HttpResponseRedirect
from Contact.models import Contact
def home(request):
    title = {
        'title':'Muzammil Ahmad Software Programmer'
    }
    try:
        if request.method=="POST":
            fname=request.POST.get('name')
            femail=request.POST.get('email')
            fsubject=request.POST.get('subject')
            fmessage=request.POST.get('message')
            query=Contact(name=fname,email=femail,subject=fsubject,message=fmessage)
            query.save()
            return HttpResponseRedirect("")
    except:
        pass
    return render(request,"index.html",title)


def detail(request):
    title = {
        'title':'Portfolio Details'
    }
    return render(request,"portfolio-details.html",title)