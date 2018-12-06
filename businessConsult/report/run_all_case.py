#coding=utf-8

import unittest
from common.HTMLTestRunner_api import HTMLTestRunner

discover = unittest.defaultTestLoader.discover("E:\\PycharmProjects\\4sSCRM\\case",
                                               "test*.py")

reportpath = "E:\\PycharmProjects\\4sSCRM\\report"+"\\report.html"

fp = open(reportpath, "wb")

runner = HTMLTestRunner(fp,
                        title="这是我的报告",
                        description="报告内容如下"
                       )
runner.run(discover)