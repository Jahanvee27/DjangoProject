from django.urls import path,re_path
from . import views

app_name='polls'

urlpatterns=[
    path('',views.index,name="index"),
    path('first_page/',views.first_page,name="first_page"),
    re_path(r'^(?P<question_id>[0-9]+)/details/$', views.details, name='details'),
    re_path(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    re_path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]