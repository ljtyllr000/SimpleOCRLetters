from django.db import models


# Create your models here.

class RecognitionRecoder(models.Model):
    upload_time = models.DateTimeField()
    file_name = models.CharField(max_length=60, default=None)
    image_str = models.TextField(default=None)
