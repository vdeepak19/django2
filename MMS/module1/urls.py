from django.urls import path, include
from . import views
from .views import function4


# app_name = 'navbar'
urlpatterns = [
    path('',views.function2, name = 'home1'),
    path('link1/',views.function1, name = 'home'),
    # path('',views.function2, name = 'home1'),
    path('link3/',views.function3, name = 'contact'),
    path('link4/', views.function4, name = 'review'),
    path('link5/',views.register1),
    path('link6/',views.function5, name = 'sdpreview'),
    path('link6/link7/',views.function6),
    path('link8/',views.login1, name = 'login'),
    path('BusinessSystem/',views.businesssystem, name = 'BusinessSystem'),
    path('klu/',views.function7),
    path('conatctus/',views.contactus1, name = 'contactus'),
    path('mail/',views.mail1, name = 'mail'),
    path('db/',views.function8, name = 'time1'),
    path('wh/',views.weatherapp),
    path('qrcode/',views.qrcode3, name = 'qrcode'),
    path('qrcode1/',views.qrcode12, name = 'qrcode1'),
    path('all/',views.alllinksfunction, name = 'alllinks'),
    path('logout/', views.logout_user, name='logout'),
    path('link9/',views.function9, name = 'login2'),
    # path('link10/' )

]
