from django.db import models

# Create your models here.
class Information(models.Model):
    name = models.CharField(max_length = 10)
    lastName = models.CharField(max_length = 10)
    address =  models.CharField(max_length = 25)
    description = models.TextField(max_length = 500)
    delivered = models.BooleanField(default = False)

    def __str__(self) :
        return self.name