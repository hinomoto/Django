from django.conf.urls import url
from . import views

# このapp_nameを追加する
app_name = "js" 
 
urlpatterns = [
    url(r'^$', views.index, name='index'),
]

