from flask import Flask, jsonify
from server import app
from server.models import User,IPResource
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json



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
    jsonify1 = jsonify(result_)
    return jsonify1


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
