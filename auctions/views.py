from django.shortcuts import render
from .models import Listing, Bid
from django.contrib.auth.decorators import login_required
from .forms import ListingForm, BidForm
from django.http import HttpResponseRedirect
from django.urls import reverse

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

# Creating new_listing view
@login_required(login_url='/users/login/')
def new_listing(request):
    """Create a new listing"""
    if request.method != "POST":
        # recive new data and make a new form null
        form = ListingForm()
    else:
        # recive full form and process
        form = ListingForm(request.POST)
        if form.is_valid():
            new_listing = form.save(commit=False)
            new_listing.owner = request.user
            new_listing.save()
            return HttpResponseRedirect(reverse('index'))
    context = { 'form' : form }
    return render(request, 'auctions/new_listing.html', context)

# Creating place_bid view
@login_required(login_url='/users/login/')
def place_bid(request, listing_id = None):
    listing = Listing.objects.get(id = listing_id)

    if request.method != 'POST':
        form = BidForm()
    else:
        form = BidForm(data = request.POST)
        if form.is_valid():
            new_bid = form.cleaned_data['bid_amount']

            max_bid = Bid.objects.filter(bid_item = listing).order_by('-bid_amount').first()

            if max_bid:
                min_bid = max_bid.bid_amount
            else:
                min_bid = listing.initial_price

        if new_bid <= min_bid:
            form.add_error('bid_amount', f"The bid must be higher than {min_bid}.")
        else:
            bid = form.save(commit=False)
            bid.bid_item = listing
            bid.bid_owner = request.user

            bid.save()

            return HttpResponseRedirect(reverse('listing', args=(listing.id,)))
    context = {
        'form' : form,
        'listing' : listing
    }
    return render(request, 'auctions/place_bid.html', context)