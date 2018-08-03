from django.conf.urls import url
from .import views

app_name='classroom'
urlpatterns = [
    url(r'^discussion/$',views.discussion,name="list"),
    url(r'^create/$',views.post_create,name="post_create"),
    url(r'^(?P<slug>[\w-]+)/$',views.post_details,name="detail"),
    
]

