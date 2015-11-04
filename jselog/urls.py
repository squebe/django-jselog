from django.conf.urls import url
from views import *


urlpatterns = [
	url(r'^jselog$', log_error),
]