from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views
from accounts import views as AccountViews

urlpatterns = [
    path('', AccountViews.vendorDashboard),
    path('profile/', views.vprofile, name="vprofile"),
 
]
