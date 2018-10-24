# coding:utf-8
import unittest
import time
from common.HTMLTestRunner_api import HTMLTestRunner

discover = unittest.defaultTestLoader.discover("D:\\sele_project_t9\\case",
                                               "test*.py")

reportpath = "D:\\sele_project_t9\\report"+"\\report.html"

fp = open(reportpath, "wb")

runner = HTMLTestRunner(fp,
                        title="这是我的报告",
                        description="报告内容如下",
                        retry=1,
                        verbosity=1)
runner.run(discover)