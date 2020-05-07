from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(blank = True, null = True)
    price = models.DecimalField(decimal_places=2,max_digits=7)
    summary = models.TextField(default='Great value and available')


    def get_absolute_url(self):
        return reverse("products:product-detail-show", kwargs={"id": self.id}) #f"/products/{self.id}/"
    #self edit
    def get_absolute_url_create(self):
        return reverse("products:product-create-view", kwargs={"id": self.id}) #f"/products/{self.id}/"