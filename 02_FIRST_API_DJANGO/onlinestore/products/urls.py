from django.urls import path
# from products.views import ProductListView, ProductDetailView
from products.views import product_list, product_detail, manifacturer_list, manifacturer_detail
urlpatterns = [
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
    path('manifacturers/', manifacturer_list, name='manifacturer-list'),
    path('manifacturers/<int:pk>/', manifacturer_detail, name='manifacturer-detail'),
    # path('', ProductListView.as_view(), name='product-list'),
    # path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]

from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
