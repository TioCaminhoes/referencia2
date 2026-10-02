from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns=[
 path('',views.home,name='home'), path('ofertas/',views.offers,name='offers'), path('oferta/<slug:slug>/',views.offer_detail,name='offer_detail'),
 path('categoria/<slug:slug>/',views.category,name='category'), path('lojas/',views.stores,name='stores'), path('cupons/',views.coupons,name='coupons'),
 path('buscar/',views.search,name='search'), path('favorito/<int:pk>/',views.toggle_favorite,name='favorite'), path('votar/<int:pk>/<int:value>/',views.vote,name='vote'),
 path('alerta/<int:pk>/',views.create_alert,name='alert'), path('carrinho/',views.cart,name='cart'), path('carrinho/adicionar/<int:pk>/',views.add_cart,name='add_cart'), path('carrinho/remover/<int:pk>/',views.remove_cart,name='remove_cart'),
 path('finalizar/',views.checkout,name='checkout'), path('minha-conta/',views.account,name='account'), path('cadastro/',views.signup,name='signup'),
 path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'), path('logout/',auth_views.LogoutView.as_view(),name='logout'),
 path('newsletter/',views.newsletter,name='newsletter'), path('contato/',views.contact,name='contact'),
]
