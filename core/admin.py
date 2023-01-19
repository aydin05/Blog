from django.contrib import admin
from .models import Post, AboutUs, SocialNetwork, Header, CallBack, Service, Projects, SubscribeNews, Category, News


# Register your models here.
class CallBackAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone_number', 'countries', 'status']
    list_filter = ['status']


admin.site.register({Post, AboutUs, SocialNetwork, Header, CallBack, Service, Projects, SubscribeNews, Category, News})

