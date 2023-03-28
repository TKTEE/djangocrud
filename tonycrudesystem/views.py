from .models import People
from django.shortcuts import render, redirect

def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        idnum = request.POST.get('idnum')

        query = People(name=name, email=email, age=age, gender=gender, idnum=idnum)
        query.save()
        return redirect("/")

    return render(request, 'index.html')

def index(request):
    data = People.objects.all()
    context = {"data": data}
    return render(request, 'index.html', context)
def deleteData(request, id):
    d = People.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")
