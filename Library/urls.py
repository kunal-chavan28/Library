"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Book.views import  *
from subscribe.views import subscribe_email
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', func),
    path('homepage/',homepage, name="home"),
    path('show-books/',get_books, name="showbook"),
    path('delete-books/ <int:id>',delete_book, name="delete"),
    path('update-books/ <int:id>',update_book, name="update"),
    path('soft-delete-books/ <int:id>',soft_delete_book, name="soft-delete"),
    path('active-books/',show_active_books, name="active-books"),
    path('innactive-books/',show_inactive_books, name="inactive-books"),
    path('restore-books/ <int:id>',restore_books, name="restore"),

    #Email
    path('email-home/',subscribe_email, name="subscribe-email")

     

]
