from django.urls import path, include

from rest_framework.routers import DefaultRouter

import api.views.default as based_views
import api.views.user as user_based_views
import api.views.categories as categories_based_views
import api.views.courses as courses_based_views
import api.views.lessons as lessons_based_views

from .yasg import urlpatterns as doc_urls

app_name = 'api'
router = DefaultRouter()

urlpatterns = [
    path('', based_views.IndexView.as_view(), name='index'),

    path('categories/', categories_based_views.CategoryListView.as_view()),
    path('categories/create', categories_based_views.CategoryCreateView.as_view()),
    path('categories/<int:pk>', categories_based_views.CategoryDetailView.as_view()),
    path('categories/edit/<int:pk>', categories_based_views.CategoryUpdateView.as_view()),

    path('courses/', courses_based_views.CourseListView.as_view()),
    path('courses/create', courses_based_views.CourseCreateView.as_view()),
    path('courses/<int:pk>', courses_based_views.CourseDetailView.as_view()),
    path('courses/edit/<int:pk>', courses_based_views.CourseUpdateView.as_view()),

    path('courses/lessons/<int:pk>', lessons_based_views.LessonViewSet.as_view({'get': 'list'})),
    path('courses/lessons/create', lessons_based_views.LessonViewSet.as_view({'post': 'create'})),
    path('courses/lessons/detail/<int:pk>', lessons_based_views.LessonViewSet.as_view({'get': 'retrieve'})),
    path('courses/lessons/edit/<int:pk>', lessons_based_views.LessonViewSet.as_view({'post': 'update'})),

    path('user/', user_based_views.UserDetailView.as_view()),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += doc_urls
