from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 

urlpatterns = [
	path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('products/<product>', views.cat_product, name="productcat"),
    path('login', views.login_page, name="login"),
    path('signup', views.register_page, name="signup"),
    path('trending', views.trending, name="trending"),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('products/<product_brand>/<product_slug>', views.product_page, name="product_page"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


# Serve media files if DEBUG is True (development mode)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files using staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
