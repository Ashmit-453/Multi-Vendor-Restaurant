from django.shortcuts import render
from django.http import HttpResponse
from vendor.models import Vendor
def home(request):
    if 'lat' in request.GET:
        lat=request.GET.get['lat']
        lng=request.GET.get['lng']
    vendors=Vendor.objects.filter(is_approved=True,user__is_active=True)[:8]
    context={
        'vendors':vendors,
                }
    return render(request,'index.html',context)