from django.shortcuts import render
from .models import Listing
# Create your views here.

# Creating Index view
def index(request):
    """Return main page of app"""

    context = {}

    return render(request, 'auctions/index.html', context)

# Creating Listing view
def listing(request):
    # Importing Listing
    listings = Listing.objects.all()

    context = { 'listing_list' : listings }

    return render(request, 'auctions/listings.html', context)

# Creating Listing_view view
def listing_view(request, listing_id):
    listing_object = Listing.objects.get(id = listing_id)

    context = { 'listing_object' : listing_object}

    return render(request, 'auctions/listing.html', context)

