from django.db import models

from .invoice import Invoice
from .item import Item


class Detail_invoice(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField()

    
    fk_invoice=models.ForeignKey(Invoice, null=True, blank=True, on_delete=models.CASCADE)
    fk_item=models.ForeignKey(Item, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Detail_invoice'
        verbose_name_plural = 'Details_invoice'

    def __srt__(self):
        return 'name: {id}'.format(name=self.id)