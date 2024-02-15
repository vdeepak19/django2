from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('login',views.login,name="login"),
    path('login1',views.login1,name="login1"),
    path('signup',views.signup,name="signup"),
    path('signup1',views.signup1,name="signup1"),
    path('about',views.about,name="about"),
    path('faq',views.faq,name="faq"),
    path('logout',views.logout,name="logout"),
]