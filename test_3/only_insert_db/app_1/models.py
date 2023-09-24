from django.contrib.auth.hashers import make_password
from django.db import models
# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    depertment = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100, primary_key=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, default='')

    ROLE_CHOICES = [
        ('student', 'Student'),
        ('faculty', 'Faculty'),
    ]
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='student',
    )

    class Meta:
        db_table = "User_infoo"

    # def save(self, *args, **kwargs):
    #     algorithm = 'pbkdf2_sha256'

    #     self.password = make_password(self.password, salt=None, hasher=algorithm)
    #     super().save(*args, **kwargs)
    
    # def __str__(self):
    #     return self.email + ' ' + self.password