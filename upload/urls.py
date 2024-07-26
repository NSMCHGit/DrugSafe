from django.urls import path
from upload import views
from django.contrib.auth import views as v
urlpatterns=[
       path('home/',views.home,name='home'),
        path('upload/', views.image_upload_view,name='index'),
        path('simlple/',views.simple_upload,name='simlple_upload'),
        path('Result/',views.Result,name='Result'),
        path('NotResult/',views.NotResult,name='NotResult')
        ]
