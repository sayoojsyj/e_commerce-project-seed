from django.urls import path
from . import views
from store.controller import authview

urlpatterns = [
    path ('',views.index,name='index'),
    # path ('signup', views.signup,name = 'signup'),
    path ('signup', authview.signup,name = 'signup'),
    # path ('login', views.loginn,name = 'login'), 
    path ('login', authview.login_view,name = 'login'),   
]
