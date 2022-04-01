from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from base import views

urlpatterns = [
    path('event',views.EventList.as_view()), #views.^
    path('event/<int:pk>',views.EventDetail.as_view()) #views.^
]
urlpatterns = format_suffix_patterns(urlpatterns)
