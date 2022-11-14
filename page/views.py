from django.shortcuts import render
from django.contrib import messages
from .models import Carousel
from .forms import CarouselFormModel
# Create your views here.

def index(request):
    context=dict()
    context['images'] = Carousel.objects.filter(status="published")
    return render(request,'home/index.html', context)

# stuff not checked
def carousel_create(request):
    context=dict()
    context ['form'] = CarouselFormModel
    if request_method== 'POST':
        print(request.POST)
        print(request.FILES.get['cover_image'])
        carousel=Carousel.objects.create(
            title=request.POST.get('title')
        )
        messages.success(request,'Birseyler eklendi ama bilemiyorum')
        return render(request,'manage/carousel_list.html',context)
        