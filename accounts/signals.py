from django.db.models.signals import post_save,pre_save,post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User

from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(pre_save, sender=Profile)
def uppercase_bio(sender, instance, **kwargs):
    
    if instance.bio:
        instance.bio = instance.bio.upper()
        
@receiver(post_delete, sender=Profile)
def profile_deleted(sender, instance, **kwargs):
    print(f'Profile for user {instance.user.username} has been deleted.')