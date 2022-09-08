from django.shortcuts import render


def index(request):
    return render(request, "fuck.html")
    # return render(request, "index.html")
