from django.shortcuts import render

# Create your views here.

#Home
def home(request,id):
    return render(request, 'index.html')


#Login