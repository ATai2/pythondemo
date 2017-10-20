from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/ippool'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


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


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user')
def get_user():
    # admin = User(username='admin', pwd='admin')
    # guest = User(username='guest', pwd='guest')
    # db.create_all()
    # db.session.add(admin)
    # db.session.add(guest)
    # db.session.commit()
    result = []
    query_all = User.query.all()

    for q in query_all:
        result.append(q.as_dict())
    result_ = {'success': 0, 'data': result}
    return jsonify(result_)


@app.route('/ip')
def get_ip():
    # admin = User(username='admin', pwd='admin')
    # a = IPResource(ip_addr='1.1.1.1', username='admin')
    # db.create_all()
    # db.session.add(a)
    #
    # db.session.commit()

    result = []
    query_all = IPResource.query.all()

    for q in query_all:
        result.append(q.as_dict())
    result_ = {'success': 0, 'data': result}
    return jsonify(result_)


if __name__ == '__main__':
    app.run()
