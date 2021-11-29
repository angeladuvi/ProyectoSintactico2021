from django.urls import path, re_path
from .views import about

app_name = 'about'

urlpatterns = [
    path("acerca-de-mi-empresa", about, name="about")
]