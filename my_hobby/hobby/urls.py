from django.urls import path
from . import views

urlpatterns = [
    path("", views.hobby_info_view, name="info"),
    path("image/", views.hobby_image_view, name="image")
]