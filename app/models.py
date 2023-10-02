from django.db import models

# Create your models here.

# Leter we can replace it with ENUM class
type_of_images = (
    ("banner","Banner"),
    ("landscape","landscape"),
    ("specific","specific"),
    ("dp","dp")
)
class Images(models.Model):
    filename = models.CharField(max_length=50)
    file = models.FileField(upload_to="uploads/")
    imagetype = models.CharField(choices=type_of_images,max_length=50,default="banner")
    description = models.TextField(default=None,null=True,max_length=500)