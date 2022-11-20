from django.shortcuts import render
from.forms import Tamu 

# Create your views here.
from . models import Guest
def index(request):
    buku_tamu = Tamu()

    context = {
        'BukuTamu':buku_tamu,
    }

    if request.method =="POST":
        Guest.objects.create(
            nim = request.POST.get('nim'),
            nama = request.POST.get('nama'),
            kegiatan = request.POST.get('kegiatan'),
        )
    return render(request,'tamu/index.html',context)