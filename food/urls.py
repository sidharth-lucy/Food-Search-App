from django.urls import path
from . import views


urlpatterns=[
    path("" , views.HomePage , name="home"),
    path("searchfood" ,views.searchFood ,name='searchFood'),
    # path("do/" , views.CreateDbFromCSV),
]