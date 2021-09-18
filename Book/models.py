from django.db import models
from django.db.models.manager import Manager

# Create your models here.
class ActiveBookManager(models.Manager):  #Custom model manager
    def get_queryset(self): #Book.objects.all()
        return super().get_queryset().filter(is_deleted = "0")

class InActiveBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = "1")

class Book(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    price =models.FloatField()
    is_published = models.BooleanField(default=False)
    published_date = models.DateField(null=True)
    is_deleted = models.CharField(max_length =1, default="0")
    active_books = ActiveBookManager()
    inactive_books = InActiveBookManager()
    objects = Manager()

       
    def __str__(self):
        return f"{self.__dict__}"

    class Meta:
        db_table = "book"    