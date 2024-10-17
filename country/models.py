from django.db import models


class Country(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="country/images/")
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
