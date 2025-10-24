from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.models import BaseModel
from .user import User


class UserProfile(BaseModel):
    """
    Profil lié à un utilisateur, contenant des informations additionnelles.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name=_("Utilisateur"),
    )

    bio = models.TextField(null=True, blank=True, verbose_name=_("Biographie"))
    date_of_birth = models.DateField(null=True, blank=True, verbose_name=_("Date de naissance"))
    gender = models.CharField(
        max_length=10,
        choices=(("male", "Homme"), ("female", "Femme"), ("other", "Autre")),
        null=True,
        blank=True,
        verbose_name=_("Genre"),
    )

    def __str__(self):
        return f"Profil de {self.user.username}"

    # Logique simple
    @property
    def age(self):
        """Calcule l'âge de l'utilisateur si la date de naissance est connue."""
        from datetime import date
        if self.date_of_birth:
            today = date.today()
            return today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )
        return None
