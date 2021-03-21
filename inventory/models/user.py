from django.db import models
from .point import Point
""" Model for Users """
class User(models.Model):
    
    

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 15)
    password = models.CharField(max_length = 16)
    cc = models.CharField(max_length= 15)
    first_name=models.CharField(max_length = 15)
    last_name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    email=models.EmailField(max_length=40)
    phone=models.CharField(max_length=13)

    
    fk_point=models.OneToOneField(Point, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __srt__(self):
        return 'name: {name} dni: {dni}'.format(name=self.first_name, dni=self.cc)
