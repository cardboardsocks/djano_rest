from django.shortcuts import render
from shoestore.models import Shoe
# Create your views here.

def index_view(request):
    shoes = Shoe.objects.all()
    return render(request, 'index.html', {"shoes": shoes})