
# Create your views here.
from hotel.models import MenuItem, Order, Reward, CustomerReview
from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse



"""

def get_order(request):

    object_list = MenuItem.objects.all()
    form = OrderForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save();
    context = {
        'form': form,
        'object_list':object_list
    }
    return render(request, 'orderform.html', context)



def orderdetails(request):

    if request.method == 'POST':
        # gives list of id of inputs
        list_of_order_items = request.POST.getlist('order_list')
        list_of_order_price = request.POST.getlist('itemprice')
        custom_food = request.POST.get('custom')
        zipped_list = zip(list_of_order_items, list_of_order_price)

    queryset = MenuItem.objects.all()

    total = 0
    for a in list_of_order_items:
        for menu in queryset:
            if a == menu.name:
                total += menu.price

    context = {
        'all_items' : queryset,
        'bill' : total,
        'custom_food' : custom_food,
        'zipped_data' : zipped_list
    }

    return render(request,'orderdetail.html',context)

"""

def menu(request):

    # else,If this is a GET (or any other method) display the menu.
    menu_items = MenuItem.objects.all()
    special_list = []
    for x in menu_items:
        special_list.append(x.order_times)

    spec = max(special_list)
    sending_list = []
    for c in menu_items:
        if c.order_times == spec:
            sending_list.append(c.name)
    context = {
        'object_list': menu_items,
        'special_items': sending_list,
    }

    return render(request, 'index.html', context)


def ordersummary(request):
    # if the method is POST save the order and redirect to order summary.
    if request.method == 'POST':

        list_of_order_items = request.POST.getlist('menuitems')
        comment = request.POST.get('custom')
        list_of_order_price = request.POST.getlist('itemprice')
        quantity = request.POST.getlist('quantity')
        menu_items = MenuItem.objects.all()
        special_list = []
        flag=0
        for x in menu_items:
            special_list.append(x.order_times)

        spec = max(special_list)
        sending_list = []
        for c in menu_items:
            if c.order_times == spec:
                sending_list.append(c.name)
                flag = 0
        for aa in quantity:
            if aa == '':
                continue
            else:
                flag = 1
                break
        if flag == 0:
            return render(request, 'index.html', {
                'object_list': menu_items,
                'special_items': sending_list,
                'error_message': "You are sending an empty order!You sure don't wanna have anything? ;)",
            })

        quantity_list =[]

        for each in quantity:
            if each != '':
                quantity_list.append(each)
                if int(each) <= 0:
                    return render(request, 'index.html', {
                        'object_list': menu_items,
                        'special_items':sending_list,
                        'error_message': "You didn't select a valid quantity.",
                    })



        for_bill_zip = zip(list_of_order_items, quantity_list)
        total = 0
        price_list = []
        queryset = MenuItem.objects.all()
        for a, b in for_bill_zip:
            for one_item in queryset:
                if a == one_item.name:
                    one_item.order_times += 1
                    one_item.save()
                    price_list.append(one_item.price*int(b))
                    total += (one_item.price * int(b))

        menu = MenuItem.objects.filter(name__in=list_of_order_items)
        p = Order.objects.create(extra_comments=comment, bill=total)
        p.order_list.set(menu)
        p.order_id = "RES" + str(p.id)
        p.save()
        order_id = p.order_id

        zipped_list = zip(list_of_order_items, price_list, quantity_list)

        context = {
            'all_items': queryset,
            'bill': total,
            'custom_food': comment,
            'zipped_data' : zipped_list,
            'order_id' : order_id,
        }

        return render(request, 'orderdetail.html', context)



def orderdetails(request,id):
    queryset = get_object_or_404(Order, id=id)
    new_bill = 0
    custom = queryset.extra_comments
    list_of_order_items = queryset.order_list.all()

    list_of_item_names = []
    list_of_item_prices = []
    for a in list_of_order_items:
        list_of_item_names.append(a.name)
        list_of_item_prices.append(a.price)
        new_bill += a.price

    queryset.bill = new_bill
    queryset.save(update_fields=['bill'])

    zipped_list = zip(list_of_item_names, list_of_item_prices)

    context = {
        'details': queryset,
        'bill': new_bill,
        'custom_food': custom,
        'zipped_data': zipped_list
    }
    return render(request, 'reorderdetail.html', context)


def orderreview(request):
    order_id = request.POST.get('orderid')
    order = get_object_or_404(Order,order_id=order_id)

    order_items = order.order_list.all()

    order_items_list = []
    for a in order_items:
        order_items_list.append(a.name)



    context = {
        'order_items_list' : order_items_list,
        'order_id':order_id
    }

    return render(request,'review.html',context)


def payment(request):
    order_id = request.POST.get('orderid')
    order = get_object_or_404(Order,order_id=order_id)

    bonus = 0.7*int(order.bill)

    context = {
        'order_id': order_id,
        'bonus' : bonus
    }

    return render(request,'payment.html',context)


def assign_bonus(request):
    order_id = request.POST.get('orderid')
    points = request.POST.get('bonus')
    number = request.POST.get('mobile')
    order_details = get_object_or_404(Order,order_id=order_id)
    try:
        old_user = get_object_or_404(Reward,mobile_no=number)
        if(order_details.claimed_reward==False):
            old_user.total_points += float(points)
            order_details.claimed_reward = True
            order_details.save()
            old_user.save()
            t_points = old_user.total_points
        else:
            t_points = old_user.total_points


    except Exception:
        new_user = Reward.objects.create(mobile_no=number)
        if(order_details.claimed_reward==False):
            new_user.total_points += float(points)
            order_details.claimed_reward = True
            order_details.save()
            new_user.save()
            t_points = new_user.total_points
        else:
            t_points = new_user.total_points

    context = {
        'order_id' : order_id,
        'current_points':points,
        'mobile_no':number,
        'total_points':t_points
    }

    return render(request,'payment_success.html',context)

def save_review(request):

    order_id = request.POST.get('orderid')
    feedback = request.POST.get('review_text')
    order = Order.objects.get(order_id=order_id)
    c = CustomerReview.objects.create(review_text=feedback)
    c.order_ref = order
    c.save()

    return render(request,'final_page.html')