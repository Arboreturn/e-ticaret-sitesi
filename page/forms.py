from django.forms import ModelForm
from .models import Carousel, Page

# Create the form class.
class CarouselFormModel(ModelForm): # forms come from model form
    class Meta:
        model = Carousel
        fields = '__all__' # Don't use this
        fields = [
            'title',
            'cover_image',
            'status',
        ]
    

class PageModelForm(ModelForm):
    class Meta:
        model=Page
        # fields = '__all__' # Don't use this
        # exclude = ['title'] # get everything except the title
        fields =[
            'title',
            'cover_image',
            'content',
            'status',
        ]
        