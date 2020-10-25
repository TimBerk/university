from django.urls import path, include

from rest_framework.routers import DefaultRouter

import api.views.user as user_based_views
import api.views.categories as categories_based_views
import api.views.lessons as lessons_based_views

from api.views.courses import CourseViewSet, UserCourses, join_to_course
from api.views.schedule import ScheduleViewSet, get_list_schedule
from api.views.group import GroupViewSet

from .yasg import urlpatterns as doc_urls

app_name = 'api'
router = DefaultRouter()

urlpatterns = [
    path('categories/', categories_based_views.CategoryListView.as_view()),
    path('categories/create', categories_based_views.CategoryCreateView.as_view()),
    path('categories/<int:pk>', categories_based_views.CategoryDetailView.as_view()),
    path('categories/edit/<int:pk>', categories_based_views.CategoryUpdateView.as_view()),

    path('courses/lessons/<int:pk>', lessons_based_views.LessonViewSet.as_view({'get': 'list'})),
    path('courses/lessons/create', lessons_based_views.LessonViewSet.as_view({'post': 'create'})),
    path('courses/lessons/detail/<int:pk>', lessons_based_views.LessonViewSet.as_view({'get': 'retrieve'})),
    path('courses/lessons/edit/<int:pk>', lessons_based_views.LessonViewSet.as_view({'post': 'update'})),

    path('schedule/calendar/', get_list_schedule),

    path('user/', user_based_views.UserDetailView.as_view()),
    path('user/session-token/', user_based_views.get_csrf),
    path('user/logout/', user_based_views.logout_view),
    path('user/courses/', UserCourses.as_view()),
    path('user/join-to-course/<int:pk>/', join_to_course),

    path('auth/', include('djoser.urls.jwt')),
]

router.register(r'courses', CourseViewSet)
router.register(r'schedule', ScheduleViewSet)
router.register(r'group', GroupViewSet)

urlpatterns += doc_urls
urlpatterns += path('', include(router.urls)),
