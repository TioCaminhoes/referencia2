from django.core.management.base import BaseCommand
from django.utils.text import slugify
from offers.models import Category,Store,Offer,Coupon
class Command(BaseCommand):
 def handle(self,*args,**kwargs):
  cats=[('Tecnologia','💻'),('Celulares','📱'),('Casa','🏠'),('Games','🎮'),('Moda','👟'),('Eletro','⚡'),('Informática','🖥️'),('Mercado','🛒')]
  stores=['Amazon','Mercado Livre','Magazine Luiza','KaBuM!','Shopee','AliExpress']
  for n,i in cats: Category.objects.get_or_create(slug=slugify(n),defaults={'name':n,'icon':i})
  for n in stores: Store.objects.get_or_create(slug=slugify(n),defaults={'name':n})
  data=[('Fone Bluetooth Premium com cancelamento de ruído','Tecnologia','Amazon',199.90,299.90,'FRETE10','https://www.amazon.com.br/'),('Smartphone 256GB 5G em oferta','Celulares','Mercado Livre',1299,1699,'APP15','https://www.mercadolivre.com.br/'),('Air Fryer 5L Digital','Casa','Magazine Luiza',299.90,449.90,'CASA20','https://www.magazineluiza.com.br/'),('SSD NVMe 1TB','Informática','KaBuM! ',389.90,599.90,'SSD10','https://www.kabum.com.br/'),('Tênis casual em promoção','Moda','Shopee',79.90,139.90,'MODA5','https://shopee.com.br/'),('Controle sem fio para PC e console','Games','Amazon',159.90,229.90,'GAME10','https://www.amazon.com.br/')]
  for title,cat,store,p,old,coupon,link in data:
   st=Store.objects.get(slug=slugify(store.strip())); ca=Category.objects.get(slug=slugify(cat)); Offer.objects.get_or_create(slug=slugify(title),defaults={'title':title,'category':ca,'store':st,'price':p,'old_price':old,'coupon':coupon,'link':link,'description':'Oferta demonstrativa para testar a plataforma.','image_url':'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=800','votes':12})
  for code,store,discount in [('APP15','Mercado Livre','15% OFF'),('CASA20','Magazine Luiza','R$20 OFF'),('GAME10','Amazon','10% OFF')]: Coupon.objects.get_or_create(code=code,defaults={'store':Store.objects.get(slug=slugify(store)),'text':'Cupom disponível em produtos selecionados','discount':discount})
  self.stdout.write(self.style.SUCCESS('Dados demonstrativos criados.'))
