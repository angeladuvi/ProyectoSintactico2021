from pathlib import Path
from django.urls.conf import path
from .views import micasa

urlpatterns = [
    path('', micasa, name='home1')
]
