from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

import contacts.views as contacts_based_views

app_name = 'contacts'

handler404 = 'courses.views.handler404'

urlpatterns = [
    path('', contacts_based_views.EmailView.as_view(), name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
