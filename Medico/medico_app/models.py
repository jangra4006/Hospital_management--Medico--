from django.db import models

# Create your models here.
class spl_db(models.Model):
    img = models.ImageField(upload_to="Photo")
    desg = models.CharField(max_length=50)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class med_camp(models.Model):
    img = models.ImageField(upload_to="medical_Camp")
    
    
class appointment3(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email=models.CharField(max_length=50)
    message=models.TextField()
    
    def __str__(self):
        return self.name