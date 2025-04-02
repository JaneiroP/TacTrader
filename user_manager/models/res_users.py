from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class ResUsers(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def send(self) -> None:
        print('sending', self.email)
        hashed_password = make_password(self.password)
        self.password = hashed_password
        self.save()

    def __str__(self):
        return self.email

    def search_by_first_name(self, first_name):
        return ResUsers.objects.filter(last_name__icontains=first_name)

    def search_by_last_name(self, last_name):
        return ResUsers.objects.filter(last_name__icontains=last_name)



