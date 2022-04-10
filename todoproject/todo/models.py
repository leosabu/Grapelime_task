from django.db import models

# Create your models here.
class todomodel(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)
    date=models.DateField(auto_now=True)
    def __str__(self):
        return self.text