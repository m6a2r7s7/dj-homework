from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_obj = Phone.objects.all()
    for p in phones_obj:
        context = {'phone.name': p.name,
                   'phone.price': p.price,
                   'phone.image': p.image,
                   'phone.release_date': p.release_date,
                   'phone.lte_exists': p.lte_exists}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones_obj = Phone.objects.all()
    for p in phones_obj:
        if slug == p.slug:
            context = {
                'phone.name': p.name,
                'phone.price': p.price,
                'phone.image': p.image,
                'phone.release_date': p.release_date,
                'phone.lte_exists': p.lte_exists
            }
    return render(request, template, context)
