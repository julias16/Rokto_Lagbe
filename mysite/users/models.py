from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.AutoField(primary_key=True)
    usertype = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    bloodgroup = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.name

