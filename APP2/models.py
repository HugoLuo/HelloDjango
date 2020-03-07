from django.db import models

# Create your models here.


class XueSheng(models.Model):
    xs_name = models.CharField(max_length=16)
    xs_age = models.IntegerField(default=1)