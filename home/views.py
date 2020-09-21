from django.shortcuts import render, HttpResponse
from . models import Destination,Contact

def home(request):
    dests = Destination.objects.all()
    return render(request, "index.html",{'dests': dests})

def destinations(request):
    dests = Destination.objects.filter()
    return render (request, 'destinations.html',{'dests': dests})


def about(request):

    return render(request, "about.html")
    

    
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        ins = Contact(name=name, email=email, subject=subject, message=message)
        ins.save()
    return render(request, "contact.html")

