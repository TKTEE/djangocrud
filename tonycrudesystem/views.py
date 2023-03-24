from django.shortcuts import render, redirect
def displayindex(request):
    return render(request, "index.html")