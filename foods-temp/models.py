from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

def validate_image_size(value):
    filesize = value.size
    if filesize > 5 * 1024 * 1024:  # 5 MB
        raise ValidationError(_("The maximum file size that can be uploaded is 5MB"))

class Food(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(
        upload_to='foods/',
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_image_size  # 5 MB
        ]
    )
    
    def __str__(self) -> str:
        return self.name