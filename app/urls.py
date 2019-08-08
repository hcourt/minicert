from django.urls import path

from app.views.certificate import *
from app.views.customer import *
from app.views import index

urlpatterns = [
    path('', index.index, name='index'),
    path('customer/<int:pk>/',
         CustomerView.as_view(),
         name='customer_index'),
    path('customer/<int:pk>/certs/',
         CustomerCertificatesView.as_view(),
         name='customer_certificates'),
    path('customer/<int:pk>/active-certs/',
         CustomerActiveCertificatesView.as_view(),
         name='customer_active_certificates'),
    path('certificate/<int:pk>/',
         CertificateView.as_view(),
         name='certificate index'),
    path('certificate/<int:pk>/activate/',
         CertificateActivateView.as_view(),
         name='certificate_activate'),
]
