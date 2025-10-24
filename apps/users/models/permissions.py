from django.db import models
from django.utils.translation import gettext_lazy as _


class UserRole(models.TextChoices):
    """Rôles des utilisateurs dans le système."""
    CUSTOMER = "customer", _("Client")
    VENDOR = "vendor", _("Vendeur")
    MANAGER = "manager", _("Manager")
    ADMIN = "admin", _("Administrateur")
