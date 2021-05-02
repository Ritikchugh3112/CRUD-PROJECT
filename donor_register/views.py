from django.shortcuts import render, redirect
from .forms import donorForm,ImageForm
from .models import Donor
from django.shortcuts import render
from .models import Image


# Create your views here.


def donor_list(request):
    context = {'donor_list': Donor.objects.all(),'image_list': Image.objects.all()}
    return render(request, "donor_register/donor_list.html", context)


def donor_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = donorForm()
            image_form=ImageForm()
        else:
            donor = Donor.objects.get(pk=id)
            form = donorForm(instance=donor)
            image_form=ImageForm(instance=Image.objects.get(pk=id))
        return render(request, "donor_register/donor_form.html", {'form': form,'image_form':image_form})
    else:
        if id == 0:
            form = donorForm(request.POST, request.FILES)
        else:
            donor = Donor.objects.get(pk=id)
            form = donorForm(request.POST, request.FILES,instance= donor)
        if form.is_valid():
            form.save()
        return redirect('/donor/list')


def donor_delete(request,id):
    donor = donor.objects.get(pk=id)
    donor.delete()
    return redirect('/donor/list')

from django.shortcuts import render,redirect
from .forms import ImageForm
from .models import Image


# Create your views here.
def index(request):
    
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,"donor_form.html",{"obj":obj})  
    else:
        form=ImageForm()    
    img=Image.objects.all()
    return render(request,"donor_form.html",{"img":img,"form":form})


