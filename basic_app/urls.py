from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("basic", views.BasicCRUDView, basename="basic")
router.register("banner", views.BannerCRUDView, basename="Banner")
router.register("clientuser", views.ClientUserCRUDView, basename="ClientUser")
router.register("clientimage", views.ClientImageCRUDView, basename="ClientImage")
router.register("portfolio", views.PortfolioCRUDView, basename="Portfolio")
router.register("review", views.ReviewCRUDView, basename="Review")
router.register("socialmedia", views.SocialMediaCRUDView, basename="SocialMedia")
router.register("priceplan", views.PricePlanCRUDView, basename="PricePlan")
router.register("contactus", views.ContactUsCRUDView, basename="ContactUs")
router.register("service", views.ServiceCRUDView, basename="Service")
router.register("showcase", views.ShowcaseCRUDView, basename="showcase")
router.register("jobtype", views.JobTypeCRUDView, basename="jobtype")

urlpatterns = [
    path("get/csrf/",views.set_csrf)

]
urlpatterns += router.urls
