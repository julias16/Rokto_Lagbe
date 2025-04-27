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


class BloodRequest(models.Model):
    name = models.CharField(max_length=100, null=True)
    blood_group = models.CharField(max_length=5)
    location = models.CharField(max_length=100)
    description = models.TextField()
    phonenumber = models.CharField(max_length=100, null=True)
    requested_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.blood_group} needed at {self.location}"


