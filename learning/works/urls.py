from django.conf.urls import url,include
from . import views

urlpatterns = [ 
    url(r'^$',views.showIndex),
    url(r'^movie/$',views.show_movie_name),
    url(r'^wenku/$',views.get_baidu_wenku),
    url(r'^wenku/exits',views.show_baidu_wenku),
    url(r'^wenku/progress',views.progress_show_wenku),
]
