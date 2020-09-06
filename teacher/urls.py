from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from django.urls import path
import teacher.views as teacher_based_views

app_name = 'teacher'

urlpatterns = [
    path('signup/', teacher_based_views.SignupView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='teacher/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='teacher/login.html'), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
