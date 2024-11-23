from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=6)
    item_name = models.CharField(max_length=200, verbose_name="Pakkumise nimi")
    item_description = models.CharField(max_length=200, verbose_name="Pakkumise lühikirjeldus")
    item_price = models.IntegerField(verbose_name="Pakkumise hind")
    item_image = models.ImageField(upload_to='items/', verbose_name="Pakkumise pilt")
    item_full_description = models.TextField(verbose_name="Pakkumise täiskirjeldus")
    



    def __str__(self):
        return self.item_name
    

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
    