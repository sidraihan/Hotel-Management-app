from hotel.models import Order, MenuItem
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id','order_id', 'order_list', 'extra_comments')


class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = ('id','name','price','is_veg','is_new','order_times')

class OrderListSerializer(serializers.ModelSerializer):
    ordered_meals = MenuItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'order_list','ordered_meals')



class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'order_list')

    def create(self, validated_data):
        meals = validated_data.pop('menuitems')
        instance = Order.objects.create(**validated_data)
        for meal in meals:
            instance.meals.add(meal)

        return instance