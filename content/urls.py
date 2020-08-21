from django.urls import path
from .views import *

app_name = 'content'
urlpatterns = [
    path('siir/', EntryList.as_view(), name='entry_list'),
    path('siir/<slug:slug>/', EntryDetail.as_view(), name='entry_detail'),
]