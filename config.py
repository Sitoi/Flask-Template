import datetime
import os

from bson import ObjectId
from flask.json import JSONEncoder


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, ObjectId):
            return str(obj)
        elif isinstance(obj, bytes):
            return obj.decode("utf-8")

        return JSONEncoder.default(self, obj)


class Base:
    APP_NAME = "Flask 项目模板（Flask Template）"
    RESTPLUS_JSON = {"cls": CustomJSONEncoder}

    @staticmethod
    def init_app(app):
        pass


class Development(Base):
    Author = "Shi Tao"
    Area = "Shanghai"
    Birthday = "1997-04-18 05:20:00"
    DEBUG = True


class Testing(Development):
    TESTING = True


class Production(Base):
    Author = os.environ.get("Author")
    Area = os.environ.get("Area")
    Birthday = os.environ.get("Birthday")


config = {
    'development': Development,
    'testing': Development,
    'production': Production,
    'default': Development
}
