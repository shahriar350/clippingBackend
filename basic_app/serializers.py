import json

import django_quill.quill
from rest_framework import serializers

from basic_app.models import Basic, Banner, ClientUser, PricePlan, Portfolio, Review, SocialMedia, \
    ContactUs, Service, ClientImage, Showcase, JobType


class BasicCRUDSerializer(serializers.ModelSerializer):
    about_us = serializers.SerializerMethodField()
    welcome_text = serializers.SerializerMethodField()
    contact_info = serializers.SerializerMethodField()
    services_page = serializers.SerializerMethodField()
    footer = serializers.SerializerMethodField()

    class Meta:
        model = Basic
        fields = "__all__"

    def get_about_us(self, instance):
        return instance.about_us.html

    def get_welcome_text(self, instance):
        return instance.welcome_text.html

    def get_footer(self, instance):
        return instance.footer.html

    def get_contact_info(self, instance):
        return instance.contact_info.html

    def get_services_page(self, instance):
        return instance.services_page.html


class BannerCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class ClientImageCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientImage
        fields = "__all__"


class ClientUserCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientUser
        fields = "__all__"


class PortfolioCRUDSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = Portfolio
        fields = "__all__"

    def get_description(self, obj):
        return obj.description.html


class ReviewCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class SocialMediaCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = "__all__"


class JobtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = "__all__"


class PricePlanCRUDSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = PricePlan
        fields = "__all__"

    def get_description(self, obj):
        return obj.description.html


class ContactUsCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"


class ShowcaseCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showcase
        fields = "__all__"


class JobTypeCRUDSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobType
        fields = "__all__"


class ServiceCRUDSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = "__all__"

    def get_description(self, instance):
        return instance.description.html
