from django.db import models

# Create your models here.
class Region(models.Model):    
    name = models.TextField()  

    def __str__(self):        
        return self.name

class Fruit(models.Model):    
    region = models.ForeignKey(Region, on_delete = models.CASCADE, related_name="fruits",)    
    name = models.TextField()
    
    def __str__(self):        
        return self.region.name