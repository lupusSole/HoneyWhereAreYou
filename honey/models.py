from django.db import models

# Create your models here.


from django.db import models
import uuid

# Create your models here.

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.subject

class Update(models.Model):
    headline = models.CharField(max_length=200)
    image = models.ImageField(upload_to='honey/updates',null=True)
    description = models.TextField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    location = models.CharField ( blank=True, null=True, max_length=200)
    dates = models.CharField(max_length=50, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.headline

class Bio(models.Model):
    title = models.CharField (blank=True, null=True, max_length=200)
    image = models.ImageField(upload_to='honey/updates',null=True)
    description = models.TextField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Picture(models.Model):
    headline = models.CharField(max_length=200)
    image = models.ImageField(upload_to='honey/updates',null=True)
    added = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.headline

class Gallery(models.Model):
    headline = models.CharField(max_length=200)
    image = models.ImageField(upload_to='honey/updates',null=True)
    added = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.headline