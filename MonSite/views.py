from django.shortcuts import render


def index(request):
    context = {
        'prenom': "nicolas",
        'age': 32
    }
    return render(request,  "monSite/templates/index.html", context=context);