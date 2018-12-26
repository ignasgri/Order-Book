from django.shortcuts import render
from turkey_orders.forms import Turkey_Orders_Form

# def base(request):
#     return render(request, "base.html")

def index(request):
    return render(request, "index.html", {
        'form' : Turkey_Orders_Form,
    })