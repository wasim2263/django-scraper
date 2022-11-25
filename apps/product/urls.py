# purchase/urls.py
from django.urls import path

from . import views
app_name = "product"
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('scrap-now', views.ProductScrapView.as_view(),  name='product-scrap'),
    # path('<int:product_id>/details', views.ProductDetailsView.as_view(),  name='product-details'),
]
