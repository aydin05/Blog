from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _


def latin_slugify(str):
    str = str.replace(" ", "-")
    str = str.replace("?", "-")
    str = str.replace(",", "-")
    str = str.replace("ə", "e")
    str = str.replace("ö", "o")
    str = str.replace("ç", "ch")
    str = str.replace("ş", "sh")
    str = str.replace("ı", "i")
    str = str.replace("ü", "u")
    str = str.replace("ğ", "gh")
    str = str.replace("İ", "i")
    str = str.replace("Ə", "e")
    str = str.replace("Ö", "o")
    str = str.replace("Ü", "u")
    return str.lower()


class Category(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    title1 = models.CharField(_("Title1"), max_length=255)
    title2 = models.CharField(_("Title2"), max_length=255)
    content = models.TextField(_("Content"), max_length=255)
    image = models.ImageField(upload_to='postimages/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class News(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(_("Content"), max_length=255)
    image = models.ImageField(upload_to='postimages/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AboutUs(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    title = models.CharField(_("Title"), max_length=255)
    image = models.ImageField(upload_to='aboutimg/')
    text = models.TextField(_("Text"), max_length=255)

    def __str__(self):
        return f'{self.name}'

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Header(models.Model):
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=25)
    email = models.EmailField(_("Email"))
    social_network_icon = models.ForeignKey('SocialNetwork', on_delete=models.CASCADE)
    logo = models.ImageField('Site logo', upload_to='logo_images')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CallBack(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read')
    )
    full_name = models.CharField(_("FullName"), max_length=100)
    email = models.EmailField(_("Email"))
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    countries = CountryField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status


class SocialNetwork(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    url = models.URLField(max_length=255)
    icon = models.ImageField(upload_to='social_network_icon')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Service(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    image = models.ImageField(upload_to='service_photos')
    content = models.TextField(_("Content"), max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'


class Projects(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    image = models.ImageField(upload_to='projects_image')
    content = models.CharField(_("Content"), max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SubscribeNews(models.Model):
    name = models.CharField(_("YourName"), max_length=100)
    email = models.EmailField(_("Email"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
