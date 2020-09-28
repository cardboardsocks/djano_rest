from django.shortcuts import render

# Create your views here.

def index_view(request):
    shoes = Shoe.objects.all()
    return render(request, 'index.html', {"shoes": shoes})