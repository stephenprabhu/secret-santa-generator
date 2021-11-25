from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100,validators=[MinLengthValidator(2,'The Name Must Be Atleast 2 Characters')])
    email = models.EmailField(max_length=250)
    group = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hasVoted = models.BooleanField(default=False)
    hasBeenAssigned = models.BooleanField(default=False)

    def __str__(self):
        return self.name