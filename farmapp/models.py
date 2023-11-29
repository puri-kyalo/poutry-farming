from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=70)
    password = models.CharField(max_length=70)

    def __str__(self):
        return self.firstname + " " + self.lastname

class Products(models.Model):
    name = models.CharField(max_length=70)
    price = models.IntegerField(default=0)
    description = models.TextField()
    type = models.CharField(max_length=70, default="layers")


    def __str__(self):
        return self.name

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=70)
    price = models.CharField(max_length=70)

    def __str__(self):
        return self.title

class Order(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    phone = models.IntegerField(default=0)
    date = models.DateTimeField()
    product = models.CharField(max_length=70)
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    subject = models.CharField(max_length=70)
    message = models.TextField()

    def __str__(self):
        return self.name

class Blog_single(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    website = models.CharField(max_length=70)
    comment = models.TextField()

    def __str__(self):
        return self.name

class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Appointment(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    phone = models.IntegerField(default=0)
    date = models.DateTimeField()
    department = models.CharField(max_length=70)
    message = models.TextField()

    def __str__(self):
        return self.name
