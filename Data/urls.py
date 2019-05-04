from django.conf.urls import url

from Data import views

urlpatterns = [
    # url(r'^$', views.home, name='home'),
    # url(r'^gallery/', views.gallery, name='gallery'),
    url(r'^detail/([0-9]+)/', views.detail, name='detail'),
]