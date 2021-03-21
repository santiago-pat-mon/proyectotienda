from django.db import models

from .item import Item

class Distributor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 25)
    address=models.CharField(max_length=50)
    nit = models.CharField(max_length= 15)
    description = models.TextField(max_length=250)
    phone=models.CharField(max_length=13)

    fk_item=models.ManyToManyField(Item)

    class Meta:
        verbose_name = 'Distributor'
        verbose_name_plural = 'Distributors'

    def __srt__(self):
        return 'name: {name} description: {description}'.format(name=self.name, description=self.description)
