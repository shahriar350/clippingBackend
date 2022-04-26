from django.conf import settings
from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe
from django_quill.fields import QuillField


class Basic(models.Model):
    website_name = models.CharField(max_length=255)
    website_logo = models.ImageField()
    welcome_text = QuillField(null=True, blank=True)
    payment_accept_text = models.CharField(max_length=255)
    payment_accept_logo = models.ImageField()
    email = models.EmailField(null=True, blank=True)
    contact_number = models.CharField(null=True, blank=True, max_length=255)
    contact_info = QuillField(null=True, blank=True)
    about_us = QuillField(null=True, blank=True)
    services_page = QuillField(null=True, blank=True)
    footer = QuillField(null=True, blank=True)

    def has_add_permission(self):
        return not Basic.objects.exists()


class Banner(models.Model):
    image = models.ImageField()
    text = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)


class JobType(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    image_before = models.ImageField(null=True, blank=True)
    image_after = models.ImageField(null=True, blank=True)
    show_front = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ClientUser(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    contact_number = models.CharField(max_length=255, null=True, blank=True)
    message = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    website_address = models.CharField(max_length=255, null=True, blank=True)
    job_type = models.ManyToManyField(JobType, related_name="get_clients")
    date_created = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=255,default="unknown")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'Name: {self.name}, Email: {self.email}'


class ClientImage(models.Model):
    client = models.OneToOneField(ClientUser, on_delete=models.CASCADE, related_name="get_client_images", null=True,
                               blank=True)
    image = models.FileField()

    def image_tag(self):
        if self.image != '':
            return mark_safe('<img src="%s%s" width="150" height="150" />' % (f'{settings.MEDIA_URL}', self.image))

    def __str__(self):
        return f'Client Name: {self.client.name}'


class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    image_before = models.ImageField()
    image_after = models.ImageField()
    description = QuillField(null=True, blank=True)
    icon = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    front_page = models.BooleanField(default=False)

    def __str__(self):
        return f'Name: {self.name}, Title: {self.short_description}'


class Review(models.Model):
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    text = QuillField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Name: {self.name}'


class SocialMedia(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    icon = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Name: {self.name}'


class PricePlan(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    description = QuillField(null=True, blank=True)
    short_description = models.TextField(null=True,blank=True)
    image_before = models.ImageField(null=True, blank=True)
    image_after = models.ImageField(null=True, blank=True)
    active = models.BooleanField(default=True)
    icon = models.ImageField(null=True,blank=True)
    def __str__(self):
        return f'Name: {self.title}, Price: {self.price}'


class ContactUs(models.Model):
    class Meta:
        verbose_name = 'Contact us'
        verbose_name_plural = 'Contact us'

    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Name: {self.name}, Email: {self.email}'


class Service(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    display_image = models.ImageField()
    compare_image_before = models.ImageField()
    compare_image_after = models.ImageField()
    description = QuillField(null=True, blank=True)
    active = models.BooleanField(default=True)
    show_front = models.BooleanField(default=True)

    def __str__(self):
        return f'Service Name: {self.name}'


class Showcase(models.Model):
    compare_image_before = models.ImageField()
    compare_image_after = models.ImageField()
    active = models.BooleanField(default=True)
    show_front = models.BooleanField(default=True)


class ImageGallery(models.Model):
    image = models.ImageField()
    date_created = models.DateTimeField(auto_now_add=True)

    def image_tag(self):
        if self.image != '':
            return mark_safe('<img src="%s%s" width="150" height="150" />' % (f'{settings.MEDIA_URL}', self.image))
