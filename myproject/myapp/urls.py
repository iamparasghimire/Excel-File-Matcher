from django.urls import path
from .views import match_excel_view

urlpatterns = [
    path("", match_excel_view, name="match_excel"),
]
