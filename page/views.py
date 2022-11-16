from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.text import slugify
from .models import Carousel,Page
from .forms import CarouselFormModel,PageModelForm
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

# User:
def index(request):
    context=dict()
    context['images'] = Carousel.objects.filter(
        status="published"
        # we must saying there is cover image
        ) # we filtered the unofficial ones
    return render(request,'home/index.html', context)


#
def manage_list(request):
    context=dict()
    return render(request,'manage/manage.html',context)


@staff_member_required
def page_list(request):
    context = dict()
    context['items'] = Page.objects.all().order_by('-pk')
    return render(request, 'manage/page_list.html', context)


def page_create(request):
    context = dict()
    context["title"]="Page Create Form"
    context['form'] = PageModelForm()
    # from django.utils.text import slugify
    if request.method == 'POST':
        print(request.FILES.get('cover_image'))
        form = PageModelForm(request.POST, request.FILES)
        if form.is_valid():
            item=form.save(commit=False)
            item.slug= slugify(item.title.replace('ı','i'))
            item.save()
        messages.success(request, 'Birseyler eklendi ')
    return render(request, 'manage/form.html', context)
        

def page_update(request, pk): # abi bana pk vermessen gelmem :)
    context = dict()
    item = Page.objects.get(pk=pk)
    context['title'] = f"{item.title } - pk:{item.pk} Page Update Form"
    context['form'] = PageModelForm(instance=item)
    if request.method == 'POST':
        form = PageModelForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            if item.slug =="":
                item.slug= slugify(item.title.replace('ı','i'))
            item.save()
            # return redirect('carousel_list')
            messages.success(request, 'guncellendi ;)')
            return redirect('page_update', pk)
    return render(request, 'manage/form.html', context)


def page_delete(request,pk):
    item=Page.objects.get(pk=pk)
    item.status="deleted"
    item.save()
    return redirect('page_list')

def page_list(request):
    context= dict()
    context['items']=Page.objects.all().order_by('-pk')
    return render(request,'manage/page_list.html',context)


# Admin:
def carousel_list(request):
    context= dict()
    context['carousel']=Carousel.objects.all().order_by('-pk')
    return render(request,'manage/carousel_list.html',context)


# stuff not checked
def carousel_update(request, pk): # abi bana pk vermessen gelmem :)
    context = dict()
    # kaft_clone.com/manage/carousel/1/edit
    # Show :
    item = Carousel.objects.get(pk=pk)
    context['title'] = f"{item.title } - pk:{item.pk} Carousel Create Form"
    context['form'] = CarouselFormModel(instance=item)
    if request.method == 'POST':
        form = CarouselFormModel(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            # return redirect('carousel_list')
            messages.success(request, 'guncellendi ;)')
            return redirect('carousel_update', pk)
    return render(request, 'manage/form.html', context)



# stuff not checked
def carousel_create(request):
    context = dict()
    context['title'] = "Carousel Create Form"
    context['form'] = CarouselFormModel()
    
    if request.method == 'POST':
        print(request.FILES.get('cover_image'))
        form = CarouselFormModel(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
        messages.success(request, 'Birseyler eklendi ama ne oldu bilemiyorum')
    return render(request, 'manage/form.html', context)
        