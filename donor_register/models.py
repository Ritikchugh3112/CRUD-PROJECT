from django.db import models

# Create your models here.
class Medicalproblem(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
            return self.title

class Donor(models.Model):
    fullname = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    bloodgroup = models.CharField(max_length=200)
    medicalproblem=models.ForeignKey(Medicalproblem,on_delete=models.CASCADE)

class Image(models.Model):
    caption=models.CharField(max_length=100)
    image=models.ImageField(upload_to="img/%y")
    def __str__(self):
        return self.caption

