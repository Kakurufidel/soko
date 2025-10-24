from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .permissions import UserRole  # import des rôles


class User(AbstractUser):
    """
    Modèle utilisateur principal du projet SOKO.
    Simple et extensible. D'autres comportements seront gérés
    dans des mixins ou des fichiers séparés.
    """
    class Meta:
        app_label = 'users'
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.CUSTOMER,
    )

    phone_number = models.CharField(
        max_length=15,
        unique=True,
        verbose_name=_("Numéro de téléphone"),
        default=0
    )

    address = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Adresse"),
    )

    identity_document = models.FileField(
        upload_to="identity_docs/",
        null=True,
        blank=True,
        verbose_name=_("Document d'identité"),
    )

    # avatar = models.ImageField(
    #     upload_to="avatars/",
    #     null=True,
    #     blank=True,
    #     verbose_name=_("Photo de profil"),
    # )

    is_active = models.BooleanField(default=True)

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username or f"Utilisateur {self.id}"

    # Helpers
    def get_full_name_or_username(self):
        full_name = f"{self.first_name} {self.last_name}".strip()
        return full_name if full_name else self.username

    def get_initials(self):
        name = self.get_full_name_or_username()
        return name[:2].upper() if name else "??"

    def has_identity_document(self):
        return bool(self.identity_document)

    def is_phone_verified(self):
        return bool(self.phone_number)

    # Raccourcis
    @property
    def is_seller(self):
        return self.role == UserRole.SELLER

    @property
    def is_customer(self):
        return self.role == UserRole.CUSTOMER

    @property
    def is_admin(self):
        return self.role == UserRole.ADMIN
