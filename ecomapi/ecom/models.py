from django.db import models

class Categories(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Cloth(models.Model):
    title=models.CharField(max_length=250)
    category=models.ForeignKey(Categories,related_name='cloths',on_delete=models.CASCADE)
    size = models.IntegerField()
    price = models.IntegerField()
    image_url = models.URLField()
    stock = models.IntegerField()
    status= models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
       ordering = ['-date_created']
    def __str__(self):
        return self.title


class Product(models.Model):
    product_tag = models.CharField(max_length=20)
    name= models.CharField(max_length=150)
    category= models.ForeignKey(Categories,related_name='products',on_delete=models.CASCADE)
    price= models.IntegerField()
    #quantity= models.IntegerField()
    stock = models.IntegerField()
    image_url = models.URLField()
    status= models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

        def __str__(self):
            return '{} {}'.format(self.product_tag,self.name)