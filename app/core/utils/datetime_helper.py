from datetime import datetime

from django.utils import timezone
from django.conf import settings


def now():
    if settings.USE_TZ:
        return timezone.now()
    else:
        return datetime.now()