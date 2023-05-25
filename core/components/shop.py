from django_unicorn.components import UnicornView, QuerySetType
from core.models import *
from django.db.models import F


class ShopView(UnicornView):
    user_orderItem: QuerySetType[OrderItem] = None
    user_order: QuerySetType[Order] = None
    user_pk: int
    user_order: int

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.user_pk = kwargs.get('user')
        self.user_order = kwargs.get('order')
        self.user_orderItem = OrderItem.objects.filter(order_id=int(self.user_order))

    def add_item(self, product_id):
        item, created = OrderItem.objects.get_or_create(order_id=int(self.user_order), product_id=product_id)
        if not created:
            item.quantity = F('quantity') + 1
        self.user_orderItem = OrderItem.objects.filter(order_id=int(self.user_order))
