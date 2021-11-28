from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view to see shopping products """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # get the bag var if it exists in the session or create one if not
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        # update quantity if bag already exists
        bag[item_id] += quantity
    else:
        # add item to the bag
        bag[item_id] = quantity
    
    # finally overwrite the var in the session with the updated version
    request.session['bag'] = bag
    # print(request.session['bag'])
    return redirect(redirect_url)
