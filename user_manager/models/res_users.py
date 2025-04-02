from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password


class ResUsers(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="resusers_set",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="resusers_set",
        blank=True
    )

    def send(self) -> None:
        print('sending', self.email)
        hashed_password = make_password(self.password)
        self.password = hashed_password
        self.save()

    def __str__(self):
        return self.email

    def search_by_first_name(self, first_name):
        return ResUsers.objects.filter(first_name__icontains=first_name)

    def search_by_last_name(self, last_name):
        return ResUsers.objects.filter(last_name__icontains=last_name)
