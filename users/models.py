from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    username = models.CharField(max_length=250, unique=True)
    bio = models.CharField(max_length=250)
    avatar = models.FileField(upload_to='user/avatar')
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female')

    ])
    subject = models.CharField(max_length=10,  choices=[
        ('he', 'He'),
        ('she', 'She'),
        ('it', 'It'),
        ('they', 'They')

    ])

    def __str__(self):
        return self.username


class Follower(models.Model):
    follower_by_user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    followee_user_id = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower_by_user', 'followee_user_id')




