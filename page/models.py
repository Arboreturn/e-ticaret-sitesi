from django.db import models

# Create your models here.

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
                            default="",)
    content = models.TextField()
    cover_image= models.ImageField(upload_to='page',null = True,blank = True) # uplaod_to = hangi klasöre gönderilsin alanı
    status = models.CharField(
        default ="draft",
        choices =STATUS,
        max_length=10,
        
    )
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)
    

