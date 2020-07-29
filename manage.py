# encoding:utf-8

from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from models import *  # 如果没有导入，就会不会创建数据库

app = Flask(__name__)
app.config.from_object('settings')
db.init_app(app)
# db.create_all(app=app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
