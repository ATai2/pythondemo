#!/usr/bin/env python
# -*- coding:utf-8 -*-

from server import db
from datetime import datetime


class Base(object):
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    pwd = db.Column(db.String(120), unique=True, nullable=False)

    # info=db.Column(db.PickleType)
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return '<User %r>' % self.username


class IPResource(db.Model, Base):
    id = db.Column(db.Integer, primary_key=True)
    ip_addr = db.Column(db.String(32), nullable=False)
    creat_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ip_addr = db.Column(db.String(32), nullable=False)
    username = db.Column(db.String(32), nullable=False, default='undefine')
    # uid = db.Column(db.Integer, db.ForeignKey('user.id'))
    # user = db.relationship('User', backref=db.backref('ips', lazy=True))


if __name__ == '__main__':
    db.create_all()
