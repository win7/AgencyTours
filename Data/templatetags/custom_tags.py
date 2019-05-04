from django import template
from Data.models import *

register = template.Library()

@register.simple_tag
def service_all():
	service = Service.objects.filter(ranking=True).order_by("title").distinct("title")
	return service