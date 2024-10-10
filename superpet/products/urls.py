from django.urls import path
from . import views

urlpatterns=[
    path('',views.products,name="products"),
     path('royal-canin/',views.royalCanin,name="royalcanin"),
      path('drools/',views.drools,name="drools"),
]

