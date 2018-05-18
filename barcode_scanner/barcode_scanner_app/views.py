from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'barcode_scanner_app/index.html')
