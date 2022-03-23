from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from core import models, actions


@receiver(post_save, sender=models.State, dispatch_uid='save_log_file')
def save_log_file(**kwargs):
    actions.StateActions.save_log_file(state=kwargs.get('instance'))


@receiver(pre_save, sender=models.SaleItem, dispatch_uid='update_sale_price')
def update_sale_price(**kwargs):
    sale_item: 'models.SaleItem' = kwargs.get('instance')
    sale_item.sale_price = sale_item.product.sale_price
