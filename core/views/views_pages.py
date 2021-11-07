from django.shortcuts import render

# Views Pages
def index(request):
    return render(request, "index.html")

