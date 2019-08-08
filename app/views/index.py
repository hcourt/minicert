from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def index(request, format=None):
    return Response({
        'customer_list': reverse('customer_list', request=request,
                                 format=format),
        'customer_index': reverse('customer_index', args=('1',),
                                  request=request,
                                  format=format),
        'customer_certificates': reverse('customer_certificates', args=('1',),
                                         request=request, format=format),
        'customer_active_certificates': reverse('customer_active_certificates',
                                                args=('1',),
                                                request=request, format=format),
        'certificates': reverse('certificate_list', request=request,
                                format=format),
        'certificate_index': reverse('certificate_index', args=('1',),
                                     request=request,
                                     format=format),
        'certificate_activate': reverse('certificate_activate', args=('1',),
                                        request=request,
                                        format=format),
    })
