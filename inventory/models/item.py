from django.db import models

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 25)
    description = models.TextField(max_length=250)
    amount = models.IntegerField()
    price = models.FloatField()


    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __srt__(self):
        return 'name: {name} description: {description}'.format(name=self.name, description=self.description)
