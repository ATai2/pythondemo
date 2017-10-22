#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest, untitled,json
from server.models import User, IPResource, Base
from flask import Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy
from server import app


# app = None
# db = None


class TestIP(unittest.TestCase):
    def setUp(self):
        # self.app=create_app('testing')
        # app = Flask(__name__)
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/ippool'
        # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        # db = SQLAlchemy(app)
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        print("setUp...")

    def tearDown(self):
        print('tearDown...')

    def test_table(self):
        self.assertEqual(0, 0)

    def test_user(self):
        user = User(username="u", pwd="pwd")
        self.assertEqual(1, 1)

    def test_hello(self):
        response = untitled.hello_world()
        print(response)
        self.assertEqual("Hello World!", response)

    def test_get_user(self):
        context = app.app_context()
        # user = untitled.get_user()
        resp = self.client.get("/user")
        print(resp.data)
        self.assertEqual(0, json.loads(str(resp.data, encoding = "utf-8"))['success'])

        # def test_base(self):
        #     base = Base()
        #     attr = {"name": "name"}
        #     base.__table__.columns = attr
        #     as_dict = base.as_dict()
        #     self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
