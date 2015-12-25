# -*- coding: utf-8 -*-
from iron_urn.systemwide import db

__author__ = 'viruzzz-kun'


class ExternalSystem(db.Model):
    __tablename__ = "ExternalSystem"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    urlPrefix = db.Column(db.String(255))


class ObjectType(db.Model):
    __tablename__ = "ObjectType"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))


class UrlRule(db.Model):
    __tablename__ = "UrlRule"

    id = db.Column(db.Integer, primary_key=True)
    externalSystem_id = db.Column(db.ForeignKey('ExternalSystem.id'))
    objectType_id = db.Column(db.ForeignKey('ObjectType.id'))
    url = db.Column(db.Text)

    externalSystem = db.relationship('ExternalSystem')
    objectType = db.relationship('ObjectType')

    def get_url_rule(self):
        return u'{0}/{1}'.format(
                self.externalSystem.urlPrefix.rstrip('/'),
                self.url.lstrip('/'),
        )

    def format(self, object_id):
        return self.get_url_rule().format(id=object_id)
