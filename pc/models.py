from django.db import models

class Users(models.Model):
    #ID
    user_id = models.CharField(max_length=16)
    #ユーザ名
    user_name = models.CharField(max_length=30)
    #パスワード
    password = models.CharField(max_length=16)
    #メールアドレス
    mail_address=models.CharField(max_length=100)


# Create your models here.
