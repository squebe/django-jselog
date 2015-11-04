from django import template
from django.core.context_processors import csrf


register = template.Library()

script = """
<script>
	var previousHandler = window.onerror;
	window.onerror = function(message, url, line, column, error) {
		var r = new XMLHttpRequest(); 
		r.open('POST', 'jselog', true);
		r.setRequestHeader('Content-Type', 'application/json');
		r.setRequestHeader('X-CSRFToken', 'CSRFTOKEN');
		r.send(JSON.stringify({'error':message + ' at ' + url + ':' + line + ':' + column}));
		if (previousHandler) {
			return previousHandler.apply(this, arguments);
		}
	};
</script>
"""
script = script.replace('\t','').replace('\n','')

@register.simple_tag(takes_context=True)
def jselogger(context):
	request = context['request']
	return script.replace('CSRFTOKEN', unicode(csrf(request)['csrf_token']))