from django.urls import path
from app.views import *
app_name='nothing'
urlpatterns=[
    path('lasya/',lasya,name='lasya'),
]