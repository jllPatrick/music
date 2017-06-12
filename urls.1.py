from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    #/music/
    #url(r'^$',views.index, name = 'index'), #if no request
    url(r'^$',views.IndexView.as_view(), name = 'index'),
    
    #/music/71/
    #/music/<album_id>/
    #url(r'^(?P<album_id>[0-9]+)/$',views.detail, name = 'detail'),
    url(r'^(?P<PK>[0-9]+)/$',views.DetailView.as_view(), name = 'detail'),
    
    #/music/<album_id>/favourite/
    #url(r'^(?P<album_id>[0-9]+)/favourite/$',views.favourite, name = 'favourite'),
]
