from django.db import models

from .point import Point
from .distributor import Distributor

class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    type_invoice = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    description = models.TextField(max_length=250)
    cost = models.FloatField()
    iva = models.FloatField()

    fk_point=models.ForeignKey(Point, null=True, blank=True, on_delete=models.CASCADE)
    fk_distributor=models.ForeignKey(Distributor, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'

    def __srt__(self):
        return 'id: {id} type: {type}'.format(id=self.id, type=self.type_invoice)
