from django.urls import path

from app.views.certificate import *
from app.views.customer import *
import app.views.customer
from app.views import index

urlpatterns = [
    path('', index.index, name='index'),
    path('customer/<int:customer_id>/',
         CustomerView.as_view(),
         name='customer_index'),
    path('customer/<int:customer_id>/certs/',
         CustomerCertificatesView.as_view(),
         name='customer_certificates'),
    path('customer/<int:customer_id>/active-certs/',
         CustomerActiveCertificatesView.as_view(),
         name='customer_active_certificates'),
    path('certificate/<int:certificate_id>/',
         CertificateView.as_view(),
         name='certificate index'),
    path('certificate/<int:certificate_id>/activate/',
         CertificateActivateView.as_view(),
         name='certificate_activate'),
]
