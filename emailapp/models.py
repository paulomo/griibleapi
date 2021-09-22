from django.db import models

class EmailDetail(models.Model):
    sender = models.CharField(max_length=200)

    def __str__(self):
        return self.sender
