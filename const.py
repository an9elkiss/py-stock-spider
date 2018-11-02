# coding:utf-8
import os


class _const:
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("can't change const %s" % name)
        if not name.isupper():
            raise self.ConstCaseError('const name "%s" is not all uppercase' % name)
        self.__dict__[name] = value


ENV_PROFILE = os.getenv("ENV")

const = _const()

if ENV_PROFILE == "pro":
    const.TUSHARE_TOKEN = '640fd047dc9ca8079402b9d51902f27a545e1c82fd7629ac78ddda36'

    const.DB_HOST = "106.15.228.141"
    const.DB_USER = "root"
    const.DB_PASSWORD = "Na8gRk"
    const.DB_NAME = "a9-stock-pro"

    const.LOG_FILE_PATH = "/usr/python/logs/py-stock-spider/py-stock-spider.log"

else:
    const.TUSHARE_TOKEN = '640fd047dc9ca8079402b9d51902f27a545e1c82fd7629ac78ddda36'

    const.DB_HOST = "106.15.228.141"
    const.DB_USER = "root"
    const.DB_PASSWORD = "Na8gRk"
    const.DB_NAME = "a9-stock-test"

    const.LOG_FILE_PATH = None

