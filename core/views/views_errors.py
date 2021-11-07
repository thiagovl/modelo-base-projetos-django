from django.shortcuts import render

# Views Errors

def handler404(request, exception):
    return render(request, '404.html', status=404)
        
def handler400(request, exception):
    return render(request, '404.html', status=404)