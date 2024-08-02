from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="home"),
    path('products/<product>', views.cat_product, name="productcat"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('trending', views.trending, name="trending"),
    path('cart', views.cart, name="cart"),
    path('products/<product_brand>/<product_slug>', views.product_page, name="product_page"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
