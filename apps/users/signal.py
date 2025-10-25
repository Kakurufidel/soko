from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.users.models import User
from apps.users.models import UserProfile
from django.utils.translation import gettext_lazy as _



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Crée automatiquement un profil utilisateur
    dès qu'un nouvel utilisateur est créé.
    """
    if created:
        UserProfile.objects.create(user=instance)
