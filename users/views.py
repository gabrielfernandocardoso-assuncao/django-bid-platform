from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    "Make register for a new user."

    # Verify if request is != post
    if request.method != 'POST':
        # render form null for to to fill in
        form = UserCreationForm()
    # request = POST
    else:
        # Process completed form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Make Login and redirect to index page
            authenticated_user = authenticate(username = new_user.username, password = request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))
    context = { 'form' : form }
    return render(request, 'users/register.html', context)

def logout_view(request):
    """Make logout of user"""
    logout(request)

    return HttpResponseRedirect(reverse('index'))