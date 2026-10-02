from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name=models.CharField(max_length=80, unique=True)
    slug=models.SlugField(unique=True)
    icon=models.CharField(max_length=10, default='🛍️')
    def __str__(self): return self.name

class Store(models.Model):
    name=models.CharField(max_length=80, unique=True)
    slug=models.SlugField(unique=True)
    logo_url=models.URLField(blank=True)
    verified=models.BooleanField(default=True)
    def __str__(self): return self.name

class Offer(models.Model):
    title=models.CharField(max_length=180)
    slug=models.SlugField(unique=True)
    store=models.ForeignKey(Store,on_delete=models.CASCADE,related_name='offers')
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name='offers')
    image_url=models.URLField(blank=True)
    old_price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    coupon=models.CharField(max_length=60,blank=True)
    link=models.URLField()
    description=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)
    votes=models.IntegerField(default=0)
    clicks=models.PositiveIntegerField(default=0)
    def discount(self):
        if self.old_price and self.old_price > self.price: return round((1-self.price/self.old_price)*100)
        return 0
    def get_absolute_url(self): return reverse('offer_detail',args=[self.slug])
    def __str__(self): return self.title

class Favorite(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='favorites')
    offer=models.ForeignKey(Offer,on_delete=models.CASCADE,related_name='favorited_by')
    class Meta: constraints=[models.UniqueConstraint(fields=['user','offer'],name='unique_favorite')]

class PriceAlert(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='price_alerts')
    offer=models.ForeignKey(Offer,on_delete=models.CASCADE,related_name='alerts')
    target_price=models.DecimalField(max_digits=10,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)

class Vote(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    offer=models.ForeignKey(Offer,on_delete=models.CASCADE)
    value=models.SmallIntegerField(default=1)
    class Meta: constraints=[models.UniqueConstraint(fields=['user','offer'],name='unique_vote')]

class Coupon(models.Model):
    code=models.CharField(max_length=50,unique=True)
    store=models.ForeignKey(Store,on_delete=models.CASCADE,related_name='coupons')
    text=models.CharField(max_length=160)
    discount=models.CharField(max_length=40)
    expires_at=models.DateTimeField(null=True,blank=True)
    active=models.BooleanField(default=True)
    def __str__(self): return self.code

class Newsletter(models.Model):
    email=models.EmailField(unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

class ContactMessage(models.Model):
    name=models.CharField(max_length=120)
    email=models.EmailField()
    subject=models.CharField(max_length=160)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    read=models.BooleanField(default=False)
