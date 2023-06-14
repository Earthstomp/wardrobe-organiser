from django.db import models
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify

# Create your models here.


class Clothing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    slug = models.SlugField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('Image', overwrite=True, format='jpg')
    image = models.CharField(max_length=1000, null=True)
    colour = models.CharField(max_length=64)  # options
    condition = models.CharField(max_length=64)  # options
    purchasedDate = models.DateTimeField()

    class Meta:
        ordering = ('-created_at')

    def __str__(self):
        return self.title

    def save(self, **args, **kwargs):
        to_assign = slugify(self.title)

        if Clothing.objects.filter(slug=to_assign).exists():
            to_assign = to_assign+str(Clothing.objects.all().count())

        self.slug = to_assign

        super().save(**args, **kwargs)
