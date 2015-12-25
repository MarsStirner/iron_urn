# -*- coding: utf-8 -*-
import flask

from iron_urn.lib import models

__author__ = 'viruzzz-kun'


def get_url(nss):
    if nss.count(':') < 2:
        return flask.abort(404)
    system_code, object_type_code, object_id = nss.split(':', 2)
    ur = models.UrlRule.query.filter(
            models.ExternalSystem.code == system_code,
            models.ObjectType.code == object_type_code,
            ).first()
    if not ur:
        if not models.ExternalSystem.query.filter(models.ExternalSystem.code == system_code).count():
            return flask.abort(404, 'External system "%s" not found' % (system_code,))
        if not models.ObjectType.query.filter(models.ObjectType.code == object_type_code).count():
            return flask.abort(404, 'Object type "%s" not found' % (object_type_code,))
        return flask.abort(500)
    return ur.format(object_id)