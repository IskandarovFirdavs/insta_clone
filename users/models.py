from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = "MALE", "Male"
        FEMALE = "FEMALE", "Female"
        NOT_GIVEN = "NOT_GIVEN", "Not_given"

    class Subject(models.TextChoices):
        HE = "HE", "He"
        SHE = "SHE", "She"
        IT = "IT", "It"
        THEY = "THEY", "They"

    bio = models.CharField(max_length=250, null=True, blank=True)
    avatar = models.ImageField(upload_to='user/avatar', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=Gender.choices)
    subject = models.CharField(max_length=10,  choices=Subject.choices, default=Subject.IT)

    def __str__(self):
        return self.username


class Follower(models.Model):
    follower_by_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followee_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')

    class Meta:
        unique_together = ('follower_by_user_id', 'followee_user_id')



class Singer(models.Model):
    fullname = models.CharField(max_length=60)

    def __str__(self):
        return self.fullname
