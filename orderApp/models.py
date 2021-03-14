from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfie(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='user_avatar', null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    def __str__(self):
        return self.user.first_name+'-'+self.user.last_name


