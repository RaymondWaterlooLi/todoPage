from django.db import models

class todoItem(models.Model):
    content = models.TextField()
    #dated_created
    #author