from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Create your models here.

def validate_image_size(value):
    filesize = value.size
    if filesize > 5 * 1024 * 1024:  # 5 MB
        raise ValidationError(_("The maximum file size that can be uploaded is 5MB"))

class Category(models.Model):
    image = models.ImageField(
        upload_to='foods/',
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_image_size  # 5 MB
        ]
    )
    name_uz = models.CharField('Categorya', max_length=50)
    name_cr = models.CharField("Туркум", max_length=50)
    name_ru = models.CharField("Категория", max_length=50)

    def __str__(self) -> str:
        return self.name_uz

class Food(models.Model):
    img=models.ImageField(upload_to='foods/')
    name_uz = models.CharField("Taom nomi", max_length=255)
    name_cr = models.CharField("Таом номи", max_length=255)
    name_ru = models.CharField("Название блюда", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    description_uz = models.TextField("Tavsifi",)
    description_cr = models.TextField("Тавсифи",)
    description_ru = models.TextField("Описание",)
    shop_rating = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return self.name_uz