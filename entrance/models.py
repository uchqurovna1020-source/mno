from django.db import models


# Create your models here.


class Kitob(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    page_count = models.IntegerField
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField()

    def __str__(self):
        return self.title
