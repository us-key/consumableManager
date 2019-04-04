from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

class AmazonItem(models.Model):
    """Amazon商品
    Amazonにおける商品の情報を管理する
    """
    name = models.CharField(
        max_length=255
    )

class Item(models.Model):
    """商品"""
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )
    image_url = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    amazon_id = models.ForeignKey(
        AmazonItem,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    purchase_count = models.PositiveSmallIntegerField(
        blank=False,
        null=False,
        default=0,
    )
    last_purchase_date = models.DateField(
        blank=True,
        null=True,
    )
    average_purchase_interval = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
    )
    next_purchase_date = models.DateField(
        blank=True,
        null=True,
    )

class ItemPurchaseHistory(models.Model):
    """商品購入履歴
    商品を購入した日付を管理する
    """
    item_id = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
    )
    history_no = models.PositiveSmallIntegerField(
        blank=False,
        null=False,
    )
    purchase_date = models.DateField(
        blank=False,
        null=False,
    )
