from django.conf.urls import url, include
from polls import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_selected_question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<user_selected_question_id>[0-9]+)/$', views.detail, name='vote'),
]
