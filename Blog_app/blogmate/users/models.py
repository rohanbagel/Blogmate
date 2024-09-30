from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile/default.jpg', upload_to='profile/', validators=[FileExtensionValidator(['jpg','png'])])
    
    def __str__(self):
        return self.user.username
    
