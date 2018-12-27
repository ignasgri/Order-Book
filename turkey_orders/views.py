from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Turkey_Orders
from .forms import Turkey_Orders_Form
 
 
def turkey_order_list(request):
    all_turkey_orders = Turkey_Orders.objects.filter(create_date__lte=timezone.now()
        ).order_by('-create_date')
    return render(request, "turkey_orders_list.html", {'all_turkey_orders': all_turkey_orders})

def turkey_order_detail(request, id):
    order_details  = get_object_or_404(Turkey_Orders, pk=id)
    # order_details.views += 1 # clock up the number of post views
    order_details.save()
    return render(request, "turkey_order_edit.html",{'order_details': order_details})

def new_turkey_order(request):
    if request.method == "POST":
        form = Turkey_Orders_Form(request.POST, request.FILES)
        if form.is_valid():
            order_details = form.save(commit=False)
            order_details.author = request.user
            order_details.create_date = timezone.now()
            order_details.save()
            return redirect(turkey_order_detail, order_details.pk)
    else:
        form = Turkey_Orders_Form(request.POST)
    return render(request, 'turkey_orders_form.html', {'form': form})

def edit_turkey_order(request, id):
   order_details = get_object_or_404(Turkey_Orders, pk=id)
   if request.method == "POST":
       form = Turkey_Orders_Form(request.POST, request.FILES, instance=order_details)
       if form.is_valid():
           order_details = form.save(commit=False)
           order_details.author = request.user
           order_details.create_date = timezone.now()
           order_details.save()
           return redirect(turkey_order_detail, order_details.pk)
   else:
       form = Turkey_Orders_Form(instance=order_details)
   return render(request, 'turkey_orders_form.html', {'form': form})