from .models import Category, Store

def global_data(request):
    cart=request.session.get('cart',{})
    return {'nav_categories':Category.objects.all()[:12],'cart_count':sum(cart.values())}
