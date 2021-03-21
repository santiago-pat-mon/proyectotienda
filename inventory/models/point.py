from django.db import models

class Point(models.Model):
    id = models.AutoField(primary_key=True)
    box_budget = models.FloatField()

    class Meta: 
        verbose_name = 'Point'
        verbose_name_plural = 'Points'

    def __srt__(self):
        return 'id: {id}'.format(id=self.id)