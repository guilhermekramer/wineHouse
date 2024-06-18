from django.db import models


class Favorite(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    wine = models.ForeignKey("Wine", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
