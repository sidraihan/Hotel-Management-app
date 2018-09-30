from django.db import models
#from moneyed import Money
from djchoices import DjangoChoices, ChoiceItem
#from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User





# Create your models here.

class RatingChoices(DjangoChoices):
    ONE_STAR = ChoiceItem(1)
    TWO_STAR = ChoiceItem(2)
    THREE_STAR = ChoiceItem(3)
    FOUR_STAR = ChoiceItem(4)
    FIVE_STAR = ChoiceItem(5)

class MenuItem(models.Model):
    name = models.CharField(max_length=50,null=False)
    price = models.IntegerField(default=0)
    is_new = models.BooleanField(verbose_name='Tick if the food item is new in the menu', default=False)
    is_veg = models.BooleanField(verbose_name='Tick if the food item is vegeterian', default=False)
    is_active = models.BooleanField(default=True)
    order_times = models.IntegerField(default=0)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name','-price']

class Order(models.Model):
    #user = models.ForeignKey(User)
    order_id = models.CharField(max_length=100, blank=True, null=True)
    order_list = models.ManyToManyField('MenuItem',related_name="order_details")
    extra_comments = models.TextField(default=None)
    bill = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    claimed_reward = models.BooleanField(default=False)

    def __str__(self):
        return str(self.order_id)

    def get_order_id(self):
        return "RES" + str(self.id)


class CustomerReview(models.Model):
    order_ref = models.ForeignKey('Order',on_delete=models.CASCADE,null=True)
    review_text = models.TextField()

    def __str__(self):
        return str(self.review_text)

class Reward(models.Model):
    mobile_no = models.IntegerField(blank=True)
    total_points = models.IntegerField(default=0)
    def __str__(self):
        return str(self.mobile_no)


class ShoppingCart(models.Model):
    menu_item = models.ForeignKey('MenuItem',on_delete='PROTECT')
    is_active = models.BooleanField(verbose_name='Tick if the cart is active', default=False)
    table_number = models.IntegerField()

    def __str__(self):
        return self.menu_item.name


