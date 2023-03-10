from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView
from .models import Product, Order, Company
from .forms import OrderForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class CompanyListView(ListView):
    model = Company
class ProductListView(ListView):
    model = Product
    
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Product.objects.filter(company__slug=slug)
    

class ProductDetailView(DetailView):
    model = Product


@method_decorator(login_required, name='dispatch')
class OrderListView(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(order_by=self.request.user)


@method_decorator(login_required, name='dispatch')
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = '/order/conformed/'

    def get_context_data(self,  object_list=None, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        context['product'] = get_object_or_404(Product, slug=self.kwargs['slug'])
        return context


    def form_valid(self, form):
        slug = self.kwargs.get('slug')
        product = Product.objects.get(slug__iexact=slug)
        form.instance.product = product
        form.instance.cost = int(form.instance.count) * int(product.price)
        return super(OrderCreateView, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class OrderDetailView(DetailView):
    model = Order


def order_conform(self):
    return render(self, 'Product/thanks.html')

