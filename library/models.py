from django.db import models
from taggit.managers import TaggableManager

class Cryptid(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    tags = TaggableManager()
    image = models.ImageField(upload_to = 'images', default = 'images/default.png')
    def __str__(self):
        return f"{self.name}: {self.description[:40]}..."

class Location(models.Model):
    cryptid = models.ForeignKey(Cryptid, on_delete = models.CASCADE)
    name = models.CharField(max_length=200)

class Sighting(models.Model):
    cryptid = models.ForeignKey(Cryptid, on_delete = models.CASCADE)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    report = models.TextField()
    date = models.DateField()



