import json
import uuid
import logging
from datetime import datetime

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings

lazy_type = type(_('ugettext_lazy'))


class ModelJSONFieldEncoder(json.JSONEncoder):
    """ 解决一些类型的字段不能序列化的问题 """

    def default(self, obj):
        str_cls = (models.Model, lazy_type, models.ImageField, uuid.UUID)
        if isinstance(obj, str_cls):
            return str(obj)
        elif isinstance(obj, datetime):
            return obj.strftime(settings.DATETIME_DISPLAY_FORMAT)
        elif isinstance(obj, (list, tuple)) and len(obj) > 0 \
                and isinstance(obj[0], models.Model):
            return [str(i) for i in obj]
        else:
            try:
                return super().default(obj)
            except TypeError:
                logging.error('Type error: ', type(obj))
                return str(obj)
