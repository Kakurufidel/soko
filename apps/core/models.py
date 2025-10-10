from django.db import models
from django.conf import settings

class BaseModel(models.Model):
    """Modèle abstrait avec des champs communs pour toutes les entités."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True 
    )

    class Meta:
        abstract = True
        ordering = ['-created_at']
