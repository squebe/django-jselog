from django.http import HttpResponse
import json
import logging
logger = logging.getLogger(__name__)


def log_error(request):
	error = json.loads(request.body).get("error")[:100]
	if error: logger.error(error)
	return HttpResponse()