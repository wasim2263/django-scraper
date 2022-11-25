from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import View

from apps.product.forms import ProductForm
from apps.product.models import Product
from apps.source.tasks import scrap_product


class ProductListView(View):
    def get(self, request):
        products = Product.objects.filter().order_by('-id')
        # TODO:: take pagination limit from .env
        pagination = Paginator(products, 30)
        context = {'products': pagination.get_page(request.GET.get('page'))}

        return render(request, 'product/product-list.html', context=context)


class ProductScrapView(View):
    def get(self, request):
        scrap_product.delay()
        return redirect('product:product-list')

