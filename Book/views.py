from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import Book
from Library.settings import EMAIL_HOST_USER
from subscribe.views import EmailMessage
# Create your views here.

# def func(request):
    # return render(request,"base.html")
    # print (request.method)
    # print("---------in function--------")
    # return HttpResponse("Hi welcome to hompage")
    # return JsonResponse({"key":"value"})
from datetime import date
def homepage(request):
    if request.method == "POST":
        data = request.POST
        if not data.get("id"):
            if data["ispub"] =="Yes":
                Book.objects.create(
                    name =data["nm"],
                    qty = data["qty"],
                    price = data["price"],
                    is_published = True,
                    published_date = date.today())
            elif data["ispub"] == "No":
                Book.objects.create(
                    name =data["nm"],
                    qty = data["qty"],
                    price = data["price"])
                  
        else:
            bid = data.get("id")
            book_obj = Book.objects.get(id=bid)
            book_obj.name = data["nm"]
            book_obj.qty = data["qty"]
            book_obj.price = data["price"]
            if data["ispub"] == "Yes":
                if book_obj.is_published:
                    pass
                else:
                    book_obj.is_published = True
                    book_obj.published_date = date.today()
                
            elif data["ispub"] == "No":
                    if book_obj.is_published == True:
                        pass
            book_obj.save() 
                         
        Msg = EmailMessage(subject='Welcome to Django Library', body=f"New Book is Created", from_email=EMAIL_HOST_USER, to=["knlchavan26@gmail.com"])            
        Msg.send(fail_silently = False) 
        return redirect("home")        

    else:
        return render(request, template_name="home.html")    


def get_books(request):
    books= Book.objects.all()
    return render(request, template_name="books.html",context={"all_books":books})

def delete_book(request, id):
    # print("delete book", id)
    Book.objects.get(id=id).delete()
    Msg = EmailMessage(subject='Welcome to Django Library', body= f"Book of id number-{id}  is deleted", from_email=EMAIL_HOST_USER, to=["knlchavan26@gmail.com"])            
    Msg.send(fail_silently = False) 
    return redirect("showbook")    

def update_book(request, id):
    book_obj = Book.objects.get(id=id)
    Msg = EmailMessage(subject='Welcome to Django Library', body= f"Book of id number-{id}  is updated", from_email=EMAIL_HOST_USER, to=["knlchavan26@gmail.com"])            
    Msg.send(fail_silently = False)
    return render(request, template_name="home.html",context={"single_book":book_obj})

def soft_delete_book(request, id):    
    book_obj = Book.objects.get(id=id)
    book_obj.is_deleted = "1"
    book_obj.save()
    Msg = EmailMessage(subject='Welcome to Django Library', body= f"Book of id number-{id}  is soft-deleted", from_email=EMAIL_HOST_USER, to=["knlchavan26@gmail.com"])            
    Msg.send(fail_silently = False)
    return redirect("showbook")

def show_active_books(request):
    # all_active_book = Book.objects.filter(is_deleted ="0")
    all_active_book = Book.active_books.all()
    return render(request, template_name="books.html",context={"all_books":all_active_book}) 

def show_inactive_books(request):
    # all_inactive_book = Book.objects.filter(is_deleted ="1")
    all_inactive_book = Book.inactive_books.all()
    return render(request, template_name="books.html",context={"all_books":all_inactive_book, "book_status": "Inactive"}) 

def restore_books(request, id):
    book_obj = Book.objects.get(id=id)
    book_obj.is_deleted = "0"
    book_obj.save()
    Msg = EmailMessage(subject='Welcome to Django Library', body= f"Book of id number-{id}  is restored", from_email=EMAIL_HOST_USER, to=["knlchavan26@gmail.com"])            
    Msg.send(fail_silently = False)
    return redirect("active-books")


    