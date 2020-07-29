# encoding:utf-8

DEBUG = True
HOSTNAME = '192.168.16.8'
PORT = '3306'
DATABASE = 'migrate_db'
USERNAME = 'root'
PASSWORD = 'password'
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
                                                                                        password=PASSWORD,
                                                                                        host=HOSTNAME, port=PORT,
                                                                                        db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRECT_KEY = 'secret'
