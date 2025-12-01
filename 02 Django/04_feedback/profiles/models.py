from django.db import models

# Create your models here.


# * Pillow needed?
class UserProfile(models.Model):
    image = models.ImageField(upload_to="images")
