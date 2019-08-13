from django.db import models

class product(models.Model):
    #ID
    id = models.CharField(max_length=16)
    #ユーザ名
    user_name = models.CharField()
    



# Create your models here.
