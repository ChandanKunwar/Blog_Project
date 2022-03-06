from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.core.validators import FileExtensionValidator

# Create your models here.

class ProfileModel(models.Model):
    user = models.OneToOneField(User,on_delete=CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile', validators=[FileExtensionValidator(['png','jpg'])])

    def __str__(self):
        return self.user.username
