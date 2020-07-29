# encoding:utf-8

from sqlalchemy import Column, Integer, String

from exts import db


class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(32), comment='用户名')
