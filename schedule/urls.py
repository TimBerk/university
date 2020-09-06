from django.urls import path

import schedule.views as schedule_based_views

app_name = 'schedule'

urlpatterns = [
    path('', schedule_based_views.index_view, name='index'),
    path('list', schedule_based_views.get_list_schedule, name='list'),
]
