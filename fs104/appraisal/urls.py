from django.urls import path
from appraisal import views

urlpatterns = [
    path('getappraisal',views.getappraisal,name='getappraisal' ),
    path('getfs104',views.getfs104,name='getfs104'),
    path('appraisaldetail',views.appraisaldetail,name='appraisaldetail'),
    path('',views.index,name='home')
]