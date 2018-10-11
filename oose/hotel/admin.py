from django.contrib import admin

# Register your models here.
from hotel.models import MenuItem, Order, CustomerReview, Reward, ShoppingCart

class MenuItemModelAdmin(admin.ModelAdmin):
    list_display = ['__str__',"price"]
    list_filter = ["price"]
    search_fields = ['name']
    class Meta:
        model = MenuItem


class RewardModelAdmin(admin.ModelAdmin):
    list_filter = ['total_points']
    search_fields = ['mobile_no']
    class Meta:
        model = Reward


admin.site.register(MenuItem,MenuItemModelAdmin)
admin.site.register(Order)
admin.site.register(CustomerReview)
admin.site.register(Reward,RewardModelAdmin)
admin.site.register(ShoppingCart)
