from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .models import *

def home(request):
    return render(request,'offers/home.html',{'offers':Offer.objects.filter(active=True).order_by('-created_at')[:12],'hot':Offer.objects.filter(active=True).order_by('-votes','-clicks')[:6],'categories':Category.objects.all()[:12],'coupons':Coupon.objects.filter(active=True)[:6]})
def offers(request):
    qs=Offer.objects.filter(active=True)
    sort=request.GET.get('sort','recent'); q=request.GET.get('q',''); cat=request.GET.get('cat','')
    if q: qs=qs.filter(Q(title__icontains=q)|Q(store__name__icontains=q)|Q(category__name__icontains=q))
    if cat: qs=qs.filter(category__slug=cat)
    if sort=='price': qs=qs.order_by('price')
    elif sort=='discount': qs=sorted(qs,key=lambda x:x.discount(),reverse=True)
    elif sort=='popular': qs=qs.order_by('-votes','-clicks')
    else: qs=qs.order_by('-created_at')
    return render(request,'offers/offers.html',{'offers':qs,'query':q,'sort':sort})
def category(request,slug):
    cat=get_object_or_404(Category,slug=slug); return render(request,'offers/offers.html',{'offers':Offer.objects.filter(active=True,category=cat).order_by('-created_at'),'query':cat.name,'sort':'recent'})
def stores(request): return render(request,'offers/stores.html',{'stores':Store.objects.all()})
def coupons(request): return render(request,'offers/coupons.html',{'coupons':Coupon.objects.filter(active=True).order_by('store')})
def search(request): return offers(request)
def offer_detail(request,slug):
    offer=get_object_or_404(Offer,slug=slug,active=True); return render(request,'offers/detail.html',{'offer':offer,'related':Offer.objects.filter(active=True,category=offer.category).exclude(pk=offer.pk)[:4],'is_favorite':request.user.is_authenticated and Favorite.objects.filter(user=request.user,offer=offer).exists()})
@login_required
def toggle_favorite(request,pk):
    offer=get_object_or_404(Offer,pk=pk); obj,created=Favorite.objects.get_or_create(user=request.user,offer=offer)
    if not created: obj.delete(); messages.info(request,'Removido dos favoritos.')
    else: messages.success(request,'Oferta salva nos favoritos!')
    return redirect(request.META.get('HTTP_REFERER','home'))
@login_required
def vote(request,pk,value):
    offer=get_object_or_404(Offer,pk=pk); v,created=Vote.objects.get_or_create(user=request.user,offer=offer,defaults={'value':1 if value>0 else -1})
    if created: offer.votes += 1 if v.value>0 else -1; offer.save(update_fields=['votes'])
    return redirect(request.META.get('HTTP_REFERER','home'))
@login_required
def create_alert(request,pk):
    offer=get_object_or_404(Offer,pk=pk); target=request.POST.get('target_price')
    if target:
        PriceAlert.objects.create(user=request.user,offer=offer,target_price=target); messages.success(request,'Alerta criado!')
    return redirect('offer_detail',offer.slug)
def add_cart(request,pk):
    cart=request.session.get('cart',{}); cart[str(pk)]=cart.get(str(pk),0)+1; request.session['cart']=cart; messages.success(request,'Oferta adicionada ao carrinho.'); return redirect(request.META.get('HTTP_REFERER','cart'))
def remove_cart(request,pk):
    cart=request.session.get('cart',{}); cart.pop(str(pk),None); request.session['cart']=cart; return redirect('cart')
def cart(request):
    cart=request.session.get('cart',{}); ids=[int(x) for x in cart]; items=Offer.objects.filter(id__in=ids,active=True); total=sum(float(o.price)*cart.get(str(o.id),0) for o in items); return render(request,'offers/cart.html',{'items':items,'cart':cart,'total':total})
def checkout(request):
    if not request.session.get('cart'): return redirect('cart')
    if request.method=='POST': request.session['cart']={}; messages.success(request,'Pedido de demonstração recebido! Nenhuma cobrança real foi feita.'); return redirect('account')
    return render(request,'offers/checkout.html')
@login_required
def account(request): return render(request,'offers/account.html',{'favorites':Favorite.objects.filter(user=request.user).select_related('offer'),'alerts':PriceAlert.objects.filter(user=request.user,active=True)})
def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid(): user=form.save(); login(request,user); return redirect('account')
    else: form=UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})
def newsletter(request):
    if request.method=='POST':
        email=request.POST.get('email','').strip()
        if email:
            Newsletter.objects.get_or_create(email=email); messages.success(request,'Pronto! Você receberá as novidades.')
    return redirect(request.META.get('HTTP_REFERER','home'))
def contact(request):
    if request.method=='POST': ContactMessage.objects.create(name=request.POST.get('name'),email=request.POST.get('email'),subject=request.POST.get('subject'),message=request.POST.get('message')); messages.success(request,'Mensagem enviada!'); return redirect('contact')
    return render(request,'offers/contact.html')
