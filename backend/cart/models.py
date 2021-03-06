from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from product.models import Product, SIZE_CHOICES

class ProductCart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, related_name='product_cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_cart')
    qty = models.PositiveSmallIntegerField(verbose_name='Quantity', default=1)
    size = models.CharField(choices=SIZE_CHOICES, max_length=1)
    checked_out = models.BooleanField(default=False)
    subtotal = models.PositiveIntegerField(null=True, blank=True, default=0)

    def __str__(self, *args, **kwargs):
        return f'{self.product} {self.size} {self.qty}'
    
    def save(self, *args, **kwargs):
        self.subtotal = int(self.product.price) * int(self.qty)
        return super(ProductCart, self).save(*args, **kwargs)

@receiver(models.signals.post_save, sender=ProductCart)
def product_cart_post_save(sender, instance, created, **kwargs):
    if instance.checked_out == False:
        carts = instance.cart.filter(checked_out=False)
        if carts.exists():
            for cart in carts:
                cart.save()

class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, related_name='cart')
    products = models.ManyToManyField(ProductCart, related_name='cart')
    checked_out = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    total = models.PositiveIntegerField(null=True, blank=True, default=0)

    def __str__(self, *args, **kwargs):
        return f'{self.user} {self.total}'

    def save(self, *args, **kwargs):
        return super(Cart, self).save(*args, **kwargs)

@receiver(models.signals.post_save, sender=Cart)
def cart_post_save(sender, instance, created, **kwargs):
    cart_total = 0
    for product in instance.products.all():
        cart_total += product.subtotal

    if not cart_total == instance.total:
        instance.total = cart_total
        instance.save()