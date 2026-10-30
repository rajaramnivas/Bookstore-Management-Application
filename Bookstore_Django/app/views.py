from django.http import request
from django.shortcuts import render,get_object_or_404

# Create your views here.
from .forms import bookForm
from .models import book

def addbook(request):
    if (request.method == 'POST'):
        form = bookForm(request.POST)      
        if form.is_valid():                
            form.save()
            return render(request, 'success.html')  
    else:
        form = bookForm()

    return render(request, "index.html", {'f': form})

def viewbooks(request):
    books=book.objects.all()
    return render(request,"viewbook.html",{"b":books})

def edit_book(request,id):
    b=get_object_or_404(book,id=id)
    if request.method=='POST':
         form = bookForm(request.POST,instance=b)
         if form.is_valid():
                form.save()
                return render(request, 'success.html') 
        
    else:
        form=bookForm()
    return render(request,"editbook.html",{"f":b})
    