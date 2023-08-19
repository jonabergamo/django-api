from django.urls import path, include
from . import urls

urlpatterns = [
    path('item/', include('base.urls')),
]