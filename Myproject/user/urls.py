from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index),
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('succes/',views.succes),
    path('signin/',views.signin),
    path('newbatches/',views.mynewbatches),
    path('ourfacility/',views.ourfacility),
    path('signup/',views.registration),
    path('feedback/',views.feedback),
    path('digital/',views.digital),
]