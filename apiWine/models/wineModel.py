from django.db import models


class Wine(models.Model):
    name = models.CharField(max_length=150)
    year = models.IntegerField()
    wine_type = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="assets/", null=True, blank=True)
