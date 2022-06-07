from django.urls import path
from kinoweb.views import test_response

urlpatterns = [
    path('test/', test_response)
]