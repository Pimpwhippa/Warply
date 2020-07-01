https://stackoverflow.com/questions/57345263/getting-datetime-when-user-logs-in
You can define a login event model 
and create instance every time a user is logged-in. Here is an example:

# models.py

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class LoginEvent(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_and_time = models.DateField(auto_now_add=True)


class Login(models.Model):
    username = models.CharField(max_length=50) 
    password = models.CharField(max_length=32)

    date_and_time = models.DateField(auto_now_add=True)

    def __str__(self):                               
        return self.username


Then in your views:

from datetime import datetime

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import authForm
from .models import Login, LoginEvent


def login_view(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        authform_data = authForm(request.POST or None)

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # here, create your event object
            login_event = LoginEvent.objects.create(user=user)
            authform_data.save()
            return HttpResponseRedirect(reverse('IP form'))
        else:
            messages.error(request,'Please provide valid credentials')
            return render (request,"first_app/login.html", context)

    else:
        return render (request,"first_app/login.html", context)


your code is helpful in the situations when there's a need to store last_login 
but i want to store datetime of each time the user logs-In. 
thnx for the reply. – Mystery Aug 4 '19 at 9:31
