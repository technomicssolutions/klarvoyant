import re
from django.conf import settings


def slug(title):
	title = re.sub(r"\s+", '_', title.lower())
	return title