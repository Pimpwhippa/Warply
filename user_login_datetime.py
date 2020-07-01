The built in User model has an attribute last_login that stores what you are asking for
Your custom user model doesn't seem to add any functionality 
that the built in user doesn't have, might be best to just use auth.User
EDIT:
To store every login time for every user would be best stored in it's own model

class UserLogin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DatetimeField(auto_now_add=True)

There is a signal sent every time a user logs in user_logged_in, 
you can hook up this signal to a function that creates a UserLogin entry 
every time a user logs in

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def my_callback(sender, request=None, user=None):
    UserLogin.objects.create(user=user)

Now you will have a UserLogin object for every login for each user

share edit 
flag 
edited Aug 4 '19 at 9:37 
answered Aug 4 '19 at 9:22 

Iain Shelvington 
13.5k1818 silver badges3030 bronze badges 
    • 
does it store the datetime everytime the user logs-in or just the datetime of last login ? – Mystery Aug 4 '19 at 9:24 
    • The datetime of the last login – Iain Shelvington Aug 4 '19 at 9:25 
    • i need to have datetime everytime the user logs-In :-\ – Mystery Aug 4 '19 at 9:26 
    • Updated my answer – Iain Shelvington Aug 4 '19 at 9:37 
    • @lain please consider your code again as it shows the error Signal receivers must accept keyword arguments (**kwargs) – Mystery Aug 4 '19 at 14:42 