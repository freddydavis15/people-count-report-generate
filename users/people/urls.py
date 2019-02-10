from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'(?P<param>.*/)', views.index, name="index"),

]

