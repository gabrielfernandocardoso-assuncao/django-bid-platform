# Create your models here.
from django.db import models
from django.contrib.auth.models import User 

# Creating Listing model:
class Listing(models.Model):
    # title
    title = models.CharField(max_length=50)
    # description
    description = models.TextField(max_length=200)
    # initial_price
    initial_price = models.FloatField()
    # date_ending
    date_endind = models.DateTimeField(auto_now_add=True)
    # owner
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
            "return representation of name"
            return self.title
    
# Creating Bid model:
class Bid(models.Model):
    # bid_amount
    bid_amount = models.FloatField()
    # bid_date
    bid_date = models.DateTimeField(auto_now_add=True)
    # bid_owner
    bid_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # bid_item 
    bid_item = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self):
        "return representation of name"
        return f"Lance de {self.bid_amount} em {self.bid_item}"
