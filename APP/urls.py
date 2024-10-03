from django.urls import path
from . import views

urlpatterns =[
    path('', views.Landing_0, name='Landing_0'),
   
    path('Register_2/', views.Register_2, name='Register_2'),
    path('Login_3/', views.Login_3, name='Login_3'),
  
    # path('output',views.output,name='output'),
    path('Logout/', views.Logout, name='Logout'),
    path('login1/', views.login1, name='login1'),
    

    path('upload_file', views.upload_file, name='upload_file'),
    path('predit', views.predit, name='predit'),

    # path('navigate', views.navigate, name='navigate'),
    path("output",views.output,name="output"),
    path("output1",views.output1,name="output1"),
]