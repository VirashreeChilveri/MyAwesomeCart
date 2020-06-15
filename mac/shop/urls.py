from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='ShopHome'),
    path('b',views.basic,name='Basic'),
    path('product',views.product,name='ProductList'),
    path('about/',views.about,name='AboutUs'),
    path('contact/',views.contact,name='ContactUs'),
    path('tracker/',views.tracker,name='TrackingStatus'),
    path('search/',views.search,name='Search'),
    path('products/<int:myid>',views.prodView,name='ProductView'),
    path('checkout/',views.checkout,name='Checkout'),
    # path('register/',views.register,name='Register'),
    path('login/',views.login,name='Login'),
    path('cart/',views.cart,name='Cart'),
    path('handlerequest/',views.handlerequest,name='HandleRequest')
    # path('wishlist/',views.wishlist,name='Wishlist'),
]