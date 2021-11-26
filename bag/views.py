from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view to see shopping products """

    return render(request, 'bag/bag.html')