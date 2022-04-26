from django.conf import settings
from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from basic_app.models import Basic, Banner, ClientUser, ClientImage, Portfolio, Review, SocialMedia, \
    PricePlan, ContactUs, Service, JobType, ImageGallery, Showcase


@admin.register(Basic)
class BasicAdmin(admin.ModelAdmin):
    model = Basic
    list_display = [
        'id',
        'website_name',
        'email',
        'contact_number'
    ]

    def has_add_permission(self, request):  # Here
        return not Basic.objects.exists()


class PricePlanAdmin(admin.StackedInline):
    model = PricePlan
    extra = 0


@admin.register(JobType)
class BasicAdmin(admin.ModelAdmin):
    model = JobType
    list_display = [
        'id',
        'name',
        'active',

    ]
    list_filter = ['active']


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    model = Banner
    list_display = ['id', 'show_image', 'active']
    readonly_fields = ['show_image']
    list_filter = ['active']

    def show_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width='200',
            height='auto',
        )
        )


@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    model = ImageGallery
    list_display = ['id', 'image', 'show_image', 'full_link', 'date_created']
    readonly_fields = ['show_image']
    search_fields = ['date_created']

    def full_link(self, obj):
        return settings.BASE_URL + obj.image.url

    def show_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width='200',
            height='auto',
        )
        )


# @admin.register(ClientImage)
class ClientImageAdmin(admin.StackedInline):
    model = ClientImage
    extra = 0
    readonly_fields = ['show_image', 'image', 'id']
    can_delete = False

    def show_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width='200',
            height='auto',
        )
        )

    def has_delete_permission(self, request, obj=None):
        return False
    # list_display = ['id', 'client']

    # list_display = ['id', 'client']


@admin.register(Showcase)
class ShowcaseImageAdmin(admin.ModelAdmin):
    model = Showcase
    list_display = [
        'id', 'show_compare_image_before', 'show_compare_image_after', 'active'
    ]
    list_filter = ['active']

    def show_compare_image_before(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.compare_image_before.url,
            width='200',
            height='auto',
        )
        )

    def show_compare_image_after(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.compare_image_after.url,
            width='200',
            height='auto',
        )
        )

    # list_display = ['id', 'client']


@admin.register(ClientUser)
class ClientUserAdmin(admin.ModelAdmin):
    model = ClientUser
    list_display = [
        'id',
        'name',
        'email',
        'contact_number',
        'completed',
        'date_created',
    ]
    readonly_fields = [
        'id',
        'name',
        'email',
        'contact_number',
        'message',
        'company_name',
        'website_address',
        'job_type',
        'date_created',
    ]

    def has_add_permission(self, request):  # Here
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    # change_form_template = "admin/client_user_change_form.html"
    inlines = (ClientImageAdmin,)
    ordering = ['-date_created']
    date_hierarchy = 'date_created'
    list_filter = ['completed']
    search_fields = ['email', 'name', 'contact_number']


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    model = Portfolio
    list_display = ['id', 'name', 'active']
    list_filter = ['active']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ['id', 'name', 'active']
    list_filter = ['active']


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    model = SocialMedia
    list_display = ['id', 'name', 'active']
    list_filter = ['active']


@admin.register(PricePlan)
class PricePlanAdmin(admin.ModelAdmin):
    model = PricePlan
    list_display = ['id', 'title', 'price', 'active']
    list_filter = ['active']


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    model = ContactUs
    list_display = ['id', 'name', 'email', 'active']
    list_filter = ['active']
    ordering = ['date_created']

    def has_change_permission(self, request, obj=None):  # Here
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = ['id', 'name', 'active', 'show_front']
    list_filter = ['active', 'show_front']
