from django.urls import path
from .views import index_view, detail_view

app_name = 'courses'

handler404 = 'courses.views.handler404'

urlpatterns = [
    path('', index_view, name='index'),
    path('course/<int:id>/', detail_view, name='detail_view'),
]
