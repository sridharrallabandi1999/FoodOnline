from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile

@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        try:
            profile = UserProfile.objects.get(user=instance)  # Fixing `get` instead of `create`
            profile.save()  # Adding parentheses to call the save method
        except UserProfile.DoesNotExist:
            # Create the user profile if it does not exist
            UserProfile.objects.create(user=instance)

def pre_save_profile_receiver(sender, instance, **kwargs):
    pass

# Note: The decorator @receiver automatically connects the signal, so you don't need to call `post_save.connect` explicitly.
