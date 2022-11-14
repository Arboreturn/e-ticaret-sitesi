from django.forms import ModelForm
from .models import Carousel

# Create the form class.
class CarouselFormModel(ModelForm): # forms come from model form
    class Meta:
        model = Carousel
        fields = '__all__' # Don't use this
        fields = [
            'title',
            'cover_image',
        ]
    
    
