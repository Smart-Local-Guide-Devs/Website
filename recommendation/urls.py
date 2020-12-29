from django.urls import path
from . import views
urlpatterns=[
   path('',views.index),
   path('read_review/',views.productOverview),
   path('write_review/',views.writeReview),
   path('login/',views.login)
]