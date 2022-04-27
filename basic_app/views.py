# Create your views here.
import json
from urllib.request import urlopen

import django_quill.quill
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from backend.mixins import IsAdminOrReadOnly
from basic_app.models import Basic, ClientUser, ClientImage, Portfolio, Review, SocialMedia, PricePlan, \
    ContactUs, Service, Banner, Showcase, JobType
from basic_app.serializers import BasicCRUDSerializer, ClientUserCRUDSerializer, \
    PortfolioCRUDSerializer, ReviewCRUDSerializer, SocialMediaCRUDSerializer, \
    PricePlanCRUDSerializer, BannerCRUDSerializer, ContactUsCRUDSerializer, \
    ServiceCRUDSerializer, ClientImageCRUDSerializer, ShowcaseCRUDSerializer, JobTypeCRUDSerializer

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class BasicCRUDView(ModelViewSet):
    serializer_class = BasicCRUDSerializer
    queryset = Basic.objects.all()
    permission_classes = [IsAdminOrReadOnly]
    # def list(self, request, *args, **kwargs):
    #     basic = Basic.objects.first()
    #     basic.welcome_text = django_quill.quill.Quill(basic.welcome_text)
    #     basic.contact_info = django_quill.quill.Quill(basic.contact_info)
    #     basic.about_us = django_quill.quill.Quill(basic.about_us)
    #     basic.services_page = django_quill.quill.Quill(basic.services_page)
    #     return Response(data=self.get_serializer(basic,context={"request": request}).data)


class BannerCRUDView(ModelViewSet):
    serializer_class = BannerCRUDSerializer
    queryset = Banner.objects.filter(active=True).all()
    permission_classes = [IsAdminOrReadOnly]


class ClientUserCRUDView(ModelViewSet):
    serializer_class = ClientUserCRUDSerializer
    queryset = ClientUser.objects.all()
    def perform_create(self, serializer):
        serializer.save(country=self.request.ipinfo.country_name)


class ClientImageCRUDView(ModelViewSet):
    serializer_class = ClientImageCRUDSerializer
    queryset = ClientImage.objects.all()
    # permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        print(self.request.geo)
        serializer.save()
        clientI = ClientUser.objects.prefetch_related('get_client_images').get(id=serializer.validated_data['client'].id)
        ctx = {
            'name': clientI.name,
            'country': clientI.country,
            'url' : settings.BASE_URL + clientI.get_client_images.image.url
        }
        message = get_template('mail.html').render(ctx)
        # message = get_template("mail.html").render(Context({
        #     'object': clientI
        # }))
        #
        print(clientI.email)
        mail = EmailMessage(
            "Order confirmation",
            message,
            clientI.email,
            ['saifullah.shahriar@gmail.com'],
        )
        mail.content_subtype = "html"
        mail.send()


class PortfolioCRUDView(ModelViewSet):
    serializer_class = PortfolioCRUDSerializer
    queryset = Portfolio.objects.filter(active=True).all()
    permission_classes = [IsAdminOrReadOnly]


class ReviewCRUDView(ModelViewSet):
    serializer_class = ReviewCRUDSerializer
    queryset = Review.objects.filter(active=True).all()
    permission_classes = [IsAdminOrReadOnly]





class SocialMediaCRUDView(ModelViewSet):
    serializer_class = SocialMediaCRUDSerializer
    queryset = SocialMedia.objects.filter(active=True).all()
    permission_classes = [IsAdminOrReadOnly]


class PricePlanCRUDView(ModelViewSet):
    serializer_class = PricePlanCRUDSerializer
    queryset = PricePlan.objects.filter(active=True).all()
    permission_classes = [IsAdminOrReadOnly]


class ContactUsCRUDView(ModelViewSet):
    serializer_class = ContactUsCRUDSerializer
    queryset = ContactUs.objects.filter(active=True).all()


class ServiceCRUDView(ModelViewSet):
    serializer_class = ServiceCRUDSerializer
    queryset = Service.objects.filter(active=True).all()
    permission_classes = [IsAdminOrReadOnly]


class ShowcaseCRUDView(ModelViewSet):
    serializer_class = ShowcaseCRUDSerializer
    queryset = Showcase.objects.filter(active=True).all()
    permission_classes = [IsAdminOrReadOnly]


class JobTypeCRUDView(ModelViewSet):
    serializer_class = JobTypeCRUDSerializer
    queryset = JobType.objects.filter(active=True).all()
    permission_classes = [IsAdminOrReadOnly]


@ensure_csrf_cookie
@api_view(['GET'])
def set_csrf(request):
    return Response(status=status.HTTP_200_OK)
