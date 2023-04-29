from django.contrib.auth.models import AbstractUser

# Add ManyToManyField for "internet points"
# Update User page with stats as well as the leaderboard

class User(AbstractUser):
   def __str__(self):
       return self.username
