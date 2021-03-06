from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class UserProfie(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='user_avatar', null=False, blank=False)
    description = models.CharField(max_length=200, null=False, blank=False)
    def __str__(self):
        return self.user.first_name+'-'+self.user.last_name

class Product(models.Model):
    title=models.CharField(max_length=128,null=False,blank=False)
    cover=models.FileField(upload_to='cover_product',null=False,blank=False)
    discripton=RichTextField()
    create_at=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

