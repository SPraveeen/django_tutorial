from django.shortcuts import render

# Create your views here.
def HomePage(request):
    data={
        "name":"praveen",
        "role":"manager",
        "numbers":[1,2,3,4,5],
        "marks":{
            "tamil":100,
            "english":90
        }
    }
    return render(request,'home.html',data)

def AboutPage(request):
    return render(request,'about.html')

def ContactPage(request):
    return render(request,'contact.html')

def ServicePage(request):
    return render(request,'service.html')
