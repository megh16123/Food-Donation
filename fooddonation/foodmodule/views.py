from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def index(request):
    fooddetail = FoodDetail.objects.all()
    form = FoodDetailForm()
    context = {
        'fooddetails': fooddetail,
        'form': form}
    if(request.method == 'POST'):
        form = FoodDetailForm(request.POST);
        if(form.is_valid()):
            form.save()
            return render(request, 'foodmodule/index.html', context)
    return render(request, 'foodmodule/index.html',context)
def user_register(request):
    return render(request, 'foodmodule/user_register.html')