from django_unicorn.components import UnicornView, QuerySetType
from core.models import Product, Order, OrderItem, Customer, UserItem
from django.db.models import F


class CartView(UnicornView):
    user_products: QuerySetType[UserItem] = None
    user_pk: int

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.user_pk = kwargs.get('user')
        self.user_products = UserItem.objects.filter(user=self.user_pk)

    def add_item(self, product_pk):
        item, created = UserItem.objects.get_or_create(user_id=self.user_pk, product_id=product_pk)
        if not created:
            item.quantity = F('quantity') + 1
            item.save()
        self.user_products = UserItem.objects.filter(user=self.user_pk)







# class CartView(UnicornView):
#     user_products: QuerySetType[OrderItem] = None
#     user_order: QuerySetType[Order] = None
#     user_pk: int
#     order: int
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(**kwargs)
#         self.user_pk = kwargs.get('user')
#         self.order = kwargs.get('order')
#         self.user_order = Order.objects.get(id=self.order, complete=False)
#         self.user_products = OrderItem.objects.filter(order_id=self.user_order)
#
#     def add_item(self, product_pk):
#         item, created = OrderItem.objects.get_or_create(product_id=product_pk, order=self.user_order)
#         if not created:
#             item.quantity = F('quantity') + 1
#             item.save()
#         self.user_products = OrderItem.objects.filter(order=self.user_order)
#

