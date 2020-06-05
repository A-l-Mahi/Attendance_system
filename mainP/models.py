from django.db import models

# Create your models here.

class save(models.Model):

    Name = models.TextField(max_length = 100)
    Regno = models.CharField(max_length = 50)

    def __str__(self):
        return "s% - s% " % (self.Name, self.Regno)