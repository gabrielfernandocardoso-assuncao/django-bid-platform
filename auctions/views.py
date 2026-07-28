from django.shortcuts import render
from .models import Listing
# Create your views here.

# Creating Index view
def index(request):
    """Return main page of app"""

    context = {}

    return render(request, 'auctions/index.html', context)

def listing(request):
    # Importing Listing
    listings = Listing.objects.all()

    context = { 'listing_list' : listings }

    return render(request, 'auctions/listings.html', context)