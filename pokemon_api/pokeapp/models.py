from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.name

class Pokemon(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
