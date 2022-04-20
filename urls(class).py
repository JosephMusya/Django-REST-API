from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from base import views

urlpatterns = [
    path('event',views.EventList.as_view()),
    path('event/<int:pk>',views.EventDetail.as_view()),
    path('user',views.UserList.as_view()),
    path('user/<int:pk>',views.UserDetail.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
