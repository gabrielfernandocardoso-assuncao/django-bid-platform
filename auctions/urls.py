from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listing/', views.listing, name='listing'),
    path('listing/<int:listing_id>/', views.listing_view, name='listing'),
    path('listing/new_listing/', views.new_listing, name='new_listing'),
    path('place_bid/<int:listing_id>/', views.place_bid, name='place_bid'),
    path('close_auction/<int:listing_id>', views.close_auction, name = 'close_auction')
]
