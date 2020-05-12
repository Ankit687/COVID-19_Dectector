from django.db import models


class userXRay(models.Model):
    xRay = models.ImageField(upload_to='Images')
