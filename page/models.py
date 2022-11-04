from django.db import models

# Create your models here.
DEFAULT_STATUS = "draft"
STATUS = [
    # sol kısım DBye yazilack
    # sağ kisim human a gozukecek
    ("draft", "Taslak"),
    ("published", "Yayinlandi"),
    ("deleted", "Silindi"),
]

class Page(models.Model):
    # title: Hakkımızda / İletişim
    # slug : title den üretilmiş urls bilgisidir -- hakkimizda / iletisim
    # sadece ilk create kısmında oluşmalıdır slug
    # content
    # cover_image
    # status
    # created_at # -- ilk oluştuğu zaman
    # updated_at  # -- her değiştiği zaman
    title =(models.CharField(max_length=200))
    slug = models.SlugField(max_length=200,
                            default=DEFAULT_STATUS)
    content = models.TextField()
    cover_image= models.ImageField(upload_to='page',null = True,blank = True) # uplaod_to = hangi klasöre gönderilsin alanı
    status = models.CharField(
        default =DEFAULT_STATUS,
        choices =STATUS,
        max_length=10,
        
    )
    createt_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)
    


# carousel alanı model    
class Carousel(models.Model): 
    title =models.CharField(max_length=200,null=True,blank=True)
    cover_image=models.ImageField(
        upload_to='carousel',
        null= True,
        blank=True
    )
    status = models.CharField(
        default =DEFAULT_STATUS,
        choices =STATUS,
        max_length=10,
        
    )
    createt_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)
