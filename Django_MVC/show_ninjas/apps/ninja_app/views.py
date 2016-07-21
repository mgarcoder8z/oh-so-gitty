from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ninja_app/index.html')

def ninja(request, color=None):
    ninja = "ninja_app/img/"
    if not color:
        ninja += "all_turtles.png"
    elif color.lower() == 'blue':
        ninja += "leonardo.jpg"
    elif color.lower() == 'red':
        ninja += "raphael.jpg"
    elif color.lower() == 'orange':
        ninja += "michelangelo.jpg"
    elif color.lower() == 'purple':
        ninja += "donatello.jpg"
    else:
        ninja += "notapril.jpg"
    context = {
        'ninja' : ninja
    }
    return render(request, 'ninja_app/index.html', context)
