from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('seoul', views.seoul, name='seoul'),
    path('healthCheck', views.healthCheck, name='healthCheck'),
    path('download_video', views.download_video, name='download_video'),
    path('logout', views.logout, name='logout'),
    path('busan', views.busan, name='busan'),
    path('daegu', views.daegu, name="daegu"),
    path('incheon', views.incheon, name='incheon'),
    path('gwangju', views.gwangju, name='gwangju'),
    path('daejeon', views.daejeon, name='daejeon'),
    path('ulsan', views.ulsan, name='ulsan'),
    path('gyeonggi', views.gyeonggi, name='gyeonggi'),
    path('gangwon', views.gangwon, name='gangwon'),
    path('northgyeongsang', views.northgyeongsang, name='northgyeongsang'),
    path('southgyeongsang', views.southgyeongsang, name='southgyeongsang'),
    path('northchungcheong', views.northchungcheong, name='northchungcheong'),
    path('southchungcheon', views.southchungcheong, name='southchungcheon'),
    path('northjeolla', views.northjeolla, name='northjeolla'),
    path('southjeolla', views.southjeolla, name="southjeolla"),
    path('jeju', views.jeju, name='jeju'),
    path('sejong', views.sejong, name='sejong'),
]