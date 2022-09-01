from . import views
from django.urls import path


urlpatterns = [

path('',views.function1,name='index.html'),
path('login/',views.login,name='login'),
path('logout',views.logout,name='logout'),
#path('detail',views.function4,name='fourth.html'),
#path('thanks',views.function5,name='fifth.html'),

]

