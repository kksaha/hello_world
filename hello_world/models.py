from django.db import models
import datetime
from django.core.validators import RegexValidator


class UserDetail(models.Model):
    alpha_char = RegexValidator(r'^[a-zA-Z]*$', 'Only alpha characters are allowed.')
    user_name = models.CharField(max_length=100, unique=True, validators=[alpha_char])
    dateOfBirth = models.DateField()

    USERNAME_FIELD = 'user_name'

    def __str__(self):
        return self.user_name