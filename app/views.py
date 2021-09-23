from django.shortcuts import render

# Create your views here.
from datetime import date
date=date.today()
def filters(request):
    d={'data':'hai PYTHon','date1':date,'count':1}
    return render(request,'filters.html',d)