from django.db import models
#For user model extension
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


# EXTEND THE USER MODEL TO INCLUDE MORE PROPERTIES BY WAY OF ONE TO ONE LINK WITH A PROFILE MODEL
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=40, blank=False)
    state = models.CharField(max_length=2, blank=False)
    zip = models.CharField(max_length=5, blank=False)
    birth_date = models.DateField(blank=True, null=True)

# Following methods hook into the User model's save signals to attach the profile.
# Will appear in responses under a profile key
# Accessible in views/serializers from instance.profile[prop]
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


