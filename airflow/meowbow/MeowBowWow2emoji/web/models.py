from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=200)
    uploadedFile = models.FileField(upload_to="image/")
    session = models.CharField(max_length=200)
    dateTimeOfUpload = models.DateTimeField(auto_now=True)