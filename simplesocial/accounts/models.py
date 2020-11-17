import django
from django.db import models
from django.contrib.auth import models
# Create your models here.


class User(models.User, models.PermissionsMixin):

    def __str__(self) -> str:
        return "@{}".format(self.username)
