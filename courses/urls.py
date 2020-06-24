from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

import courses.views.courses as courses_based_views

app_name = 'courses'

handler404 = 'courses.views.handler404'

urlpatterns = [
    path('', courses_based_views.AllCoursesListView.as_view(), name='index'),
    path('courses/create/', courses_based_views.CourseCreateView.as_view(), name='create_view'),
    path('courses/<int:pk>/update/', courses_based_views.CourseUpdateView.as_view(), name='update_view'),
    path('courses/<int:pk>/delete', courses_based_views.CourseDeleteView.as_view(), name='delete_view'),
    path('courses/<int:pk>/', courses_based_views.CourseDetailView.as_view(), name='detail_view'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
