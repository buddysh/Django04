from django.conf.urls import url

from app import views

urlpatterns=[
    url('^$',views.index,name='index'),
    url('^testpageadfadfadsf/$',views.testpage,name='testpage'),
    url('^addstu/$',views.addstu,name='addstu'),
]